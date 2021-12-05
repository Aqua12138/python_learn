#excle存储
# import requests
# from bs4 import BeautifulSoup
# import openpyxl
# headers = {
#     'origin':'https://y.qq.com',
#     # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
#     'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
#     # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
#     # 标记了请求从什么设备，什么浏览器上发出
#     }
# wb=openpyxl.Workbook()
# sheet=wb.active
# sheet.title='zhx'
# sheet['A1']='序号'
# sheet['B1']='电影中文名称'
# sheet['C1']='电影英文名称'
# sheet['D1']='演员'
# sheet['E1']='别名'
# sheet['F1']='评分'
# sheet['G1']='简介'
# for j in range(0,250,25):
#     url='https://movie.douban.com/top250?start='+str(j)+'&filter='
#     res=requests.get(url=url,headers=headers)
#     soup=BeautifulSoup(res.text,'html.parser')
#     body=soup.find_all('div',class_='item')
#     for i in body:
#         try:
#             order=i.find('em',class_='')
#             title=i.find_all('span',class_='title')
#             B=order.text+'.'
#             C=title[0].text
#             D=title[1].text
#             E=i.find('span',class_='other').text
#             F=i.find('p',class_='').text[25:]
#             G=i.find('span',class_='rating_num').text
#             A=i.find('span',class_="inq").text
#             sheet.append([B,C,D,E,F,G,A])
#         except:
#             sheet.append([B,C,D,E,F,G,'无简介'])
# wb.save('豆瓣.xlsx')


#csv存储
import requests
from bs4 import BeautifulSoup
import csv
headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
# wb=openpyxl.Workbook()
# sheet=wb.active
# sheet.title='zhx'
# sheet['A1']='序号'
# sheet['B1']='电影中文名称'
# sheet['C1']='电影英文名称'
# sheet['D1']='别名'
# sheet['E1']='演员'
# sheet['F1']='评分'
# sheet['G1']='简介'
with open('豆瓣.csv', 'w', newline='', encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow(['序号','电影中文名称','电影英文名称','别名','演员','评分','简介'])
    for j in range(0,240,25):
        url='https://movie.douban.com/top250?start='+str(j)+'&filter='
        res=requests.get(url=url,headers=headers)
        soup=BeautifulSoup(res.text,'html.parser')
        body=soup.find_all('div',class_='item')
        for i in body:
            try:
                order=i.find('em',class_='')
                title=i.find_all('span',class_='title')
                B=order.text+'.'
                C=title[0].text
                D=title[1].text
                E=i.find('span',class_='other').text
                F=i.find('p',class_='').text[25:]
                G=i.find('span',class_='rating_num').text
                A=i.find('span',class_="inq").text
                # sheet.append([B,C,D,E,F,G,A])
                writer.writerow([B,C,D,E,F,G,A])
            except:
                writer.writerow([B,C,D,E,F,G,'无简介'])









