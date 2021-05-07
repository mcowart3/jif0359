import requests
from bs4 import BeautifulSoup

URL = "https://www.gutenberg.org/files/37387/37387-h/37387-h.htm"
page = requests.get(URL)
#soup = BeautifulSoup(page.content, 'html.parser')
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify)

texts = soup.find_all('p', class_ = "dropcap")
addresses = soup.find_all('p', class_ = "center")

#count = 1
#for i in texts:
    #print(i)

count = 1
#for j in addresses:
    #if count > 21  and count < 149:
       # print(j)
    #count += 1
#results = soup.find(id='

fname = "scraped_letters.py"
#data = 5

#with open(fname, 'w') as f:
    #f.write('data = {}'.format(data))
with open(fname, 'w', encoding="utf-8") as f:
    f.write("letters_list = [ \n")

count = 1
for j in addresses:
    if count > 21  and count < 149:
        with open(fname, 'a', encoding="utf-8") as f:
            f.write("\n")
            f.write("    ")
            f.write("{")
            f.write("\n")
            f.write("    ")
            f.write("    ")
            f.write("'id_': '{}'".format(count - 15))
            f.write(",")
            f.write("\n")
            f.write("    ")
            f.write("    ")
            countmod = count - 21
            f.write("'text': '''{}'''".format(texts[countmod].text.replace("\n", "")))
            f.write(",")
            f.write("\n")
            f.write("    ")
            f.write("    ")
            f.write("'title': '{}'".format(j.text))
            f.write("\n")
            f.write("    ")
            f.write("},")
            f.write("\n")
            f.write("\n")
    count += 1
                    
with open(fname, 'a', encoding="utf-8") as f:
    f.write("]")



