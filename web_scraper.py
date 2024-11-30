import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()

browser.open('https://github.com/')
print(browser.page)