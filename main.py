import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

driver.get('https://oxylabs.io/')


results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
driver.quit()

for a in soup.findAll(class_='css-1u9wo24 e115oe510'):
    name = a.find('h2')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(class_='css-1u9wo24 e115oe510'):
    date = b.find('span')
    if date not in results:
        other_results.append(date.text)

df = pd.DataFrame({'Names': results, 'Dates': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')