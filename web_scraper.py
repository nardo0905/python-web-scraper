from bs4 import BeautifulSoup
import requests
import re

def scrape(search_term):
    fixed_search_term = str(search_term).replace(' ', '+')
    
    url = f"https://www.newegg.ca/p/pl?d={fixed_search_term}&N=4131"
    page = requests.get(url).text
    doc = BeautifulSoup(page, 'html.parser')
    
    page_text = doc.find(class_="list-tool-pagination-text").strong
    pages = int(str(page_text).split('/')[-2].split(">")[-1][:-1])
    
    items_found = {}
    
    for page in range(1, pages + 1):
        url = f"https://www.newegg.ca/p/pl?d={fixed_search_term}&N=4131&page={page}"
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")
        
        div = doc.find(class_="item-cells-wrap border-cells short-video-box items-list-view is-list")
        
        items = div.find_all(string=re.compile(search_term, re.IGNORECASE))
        
        for item in items:
            parent = item.parent
            if parent.name != "a":
                continue
            
            link = parent['href']
            next_parent = item.find_parent(class_="item-container")
            try:
                price = next_parent.find(class_="price-current").find("strong").string
                items_found[item] = {"price": int(price.replace(",", "")), "link": link}
            except:
                pass
            
        sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])
            
        return sorted_items