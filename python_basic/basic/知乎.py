# import requests
# from bs4 import BeautifulSoup
# import csv
# url='https://www.zhihu.com/people/zhang-jia-wei/posts?page=1'
# headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# # params=
# A=[]
# B=[]
# p=''
# res_artical=requests.get(url=url,headers=headers)
# soup_artical=BeautifulSoup(res_artical.text,'html.parser')
# all=soup_artical.find_all('div',class_='List-item')
# with open('知乎.csv','w',newline='',encoding='utf-8') as f:
#     writer=csv.writer(f)
#     for i in all:
#         title=i.find('a').text
#         A.append(title)
#     writer.writerow(A)
#     for i in all:
#         password=i.find('span',class_='RichText ztext CopyrightRichText-richText').text
#         for k in range(0,200,20):
#             print(str(password[k:k+20])+'\n')
    
import requests
import json
#引入requests
headers={
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
#封装headers
url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?include=data%5B*%5D.comment_count%2Csuggest_edit%2Cis_normal%2Cthumbnail_extra_info%2Cthumbnail%2Ccan_comment%2Ccomment_permission%2Cadmin_closed_comment%2Ccontent%2Cvoteup_count%2Ccreated%2Cupdated%2Cupvoted_followees%2Cvoting%2Creview_info%2Cis_labeled%2Clabel_info%3Bdata%5B*%5D.vessay_info%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B*%5D.author.vip_info%3B&offset=10&limit=10&sort_by=created'
params={
'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].vessay_info;data[*].author.badge[?(type=best_answerer)].topics;data[*].author.vip_info',
'offset': '10',
'limit':'10',
'sort_by': 'created'
}
#写入网址
#封装参数
res=requests.get(url=url,headers=headers)
#发送请求，并把响应内容赋值到变量res里面
#确认这个response对象状态正确    
articles=res.json()
#用json()方法去解析response对象，并赋值到变量articles上面，此时的articles是一个
#打印这个json文件
print(articles)
# data=articles['data']
# #取出键为data的值。
# for i in data:
#     print(i['title'])
    #遍历列表，拿到的是列表里的每一个元素，这些元素都是字典，再通过键把值取出来


            

        

        


             
        
