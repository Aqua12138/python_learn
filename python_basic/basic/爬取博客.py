from bs4 import BeautifulSoup
import requests #调用requests库
res1 = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn')
#获取网页源代码，得到的res是Response对象
soup=BeautifulSoup(res1.text,'html.parser')
result1=soup.find('ul',id='recentcomments')#一次锁定内容
#把res的内容以字符串的形式返回
print('响应状态码:',res1.status_code) #检查请求是否正确响应
# title = result1.find_all('li',class_='recentcomments')#二次内容锁定
# with open('22.txt','w') as f:
#     for i in title:
#         data=i.find('a')#锁定行
#         internet=data['href']#读取当行属性值
#         res2=requests.get(internet)
#         soup=BeautifulSoup(res2.text,'html.parser')
#         result2=soup.find('div',class_='entry-content')#锁定内容
#         content=result2.text#读取内容里所有文本
#         f.write(content+'\n\n\n\n\n')




        


        



