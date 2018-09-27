import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request

url = 'https://alpha.wallhaven.cc/search?q=islamic&categories=111&purity=100&sorting=relevance&order=desc&page='
driver = webdriver.Chrome(executable_path="D:\installed\chromedriver")
links = []

for i in range(1,8):
    m_url = url + str(i)
    driver.get(m_url)
    
    # html_doc = request.urlopen(m_url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # print(soup)

    figures = soup.find_all('figure', class_ = 'thumb-sfw')

    for figure in figures:
        try:
            a = figure.find('a', class_ = 'preview')
            links.append(a['href'])
        except:
            continue


# print(links)

img_link = []

for link in links:
    driver.get(link)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    try:
        img = soup.find('div', class_ = 'scrollbox')
        img = img.find('img')
        img_link.append('http:' + img['src'])
    except:
        continue

for img in img_link:
    print(img)

num = 1
for img in img_link:
    f = open(str(num) + '.jpg' , 'wb')
    f.write(requests.get(img).content)
    num+=1
    f.close()

driver.quit()
