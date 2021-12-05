from bs4 import BeautifulSoup
import requests 
headers={'user-agent':'Mozilla/5.0'}
res=requests.get('http://www.xiachufang.com/explore/',headers=headers)
html=res.text
soup=BeautifulSoup(html,'html.parser')
title=soup.find_all('div',class_='info pure-u')
with open('33.txt', 'w') as f:
    for i in title:
        name=i.find('a')
        f.write(name.text)
        menu=i.find('p',class_='ing ellipsis')
        menu_single=menu.find_all('a')
        for j in menu_single:
            f.write(j.text+'\t')
        f.write('\n'+'https://www.xiachufang.com/'+name['href'])



        


