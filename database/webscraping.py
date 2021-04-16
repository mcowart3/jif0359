from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://quod.lib.umich.edu/e/eebo/A36298.0001.001/1:4?rgn=div1;view=fulltext")

content = driver.page_source
soup = BeautifulSoup(content, 'lxml')

i = 0
for letter in soup.find_all('div', class_ = 'textindentlevelx'):
    i += 1
    fp = open("letter" + str(i) + ".txt", "w", encoding="utf-8")
    fp.write(letter.text)
    fp.close()

driver.close()