import requests
import openpyxl
# 引用requests库
url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
}
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='zhx'
sheet['A1']='歌曲名称'
sheet['B1']='专辑'
sheet['C1']='时长'
sheet['D1']='播放链接'
for i in range(1,6):
    params={
    'ct': '24',
    'qqmusic_ver': '1298',
    'new_json': '1',
    'remoteplace': 'txt.yqq.top',
    'searchid': '1',
    't': '0',
    'aggr': '1',
    'cr': '1',
    'catZhida': '1',
    'lossless': '0',
    'flag_qc': '0',
    'p': str(i),
    'n': '10',
    'w': '周杰伦',
    '_': '1620636082204',
    'cv': '4747474',
    'ct': '24',
    'format': 'json',
    'inCharset': 'utf-8',
    'outCharset': 'utf-8',
    'notice': '0',
    'platform': 'yqq.json',
    'needNewCode': '0',
    'uin': '0',
    'g_tk_new_20200303': '5381',
    'g_tk': '5381',
    'hostUin': '0',
    'loginUin': '0'
    }
    res_music = requests.get(url=url,params=params,headers=headers)
    #调用get方法，下载这个字典
    json_music = res_music.json()
    print( type(json_music))
    # 使用json()方法，将response对象，转为列表/字典
    A=json_music['data']['song']['list']
    for i in A:
        sheet.append([str(i['name']),str(i['album']['name']),str(i['interval']),'https://y.qq.com/n/yqq/song/' + str(i['file']['media_mid']) + '.html\n\n'])
wb.save('first.xlsx')


# import requests
# # 引用requests模块
# url ='https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
# url2='https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
# last='song_648242_3404764655_1620400445'
# headers = {
#     'origin':'https://y.qq.com',
#     # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
#     'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
#     # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
#     # 标记了请求从什么设备，什么浏览器上发出
#     }
# with open('55.txt','w') as f:
#     for i in range(5):  
#         params = {
#         'g_tk_new_20200303': '5381',
#         'g_tk':'5381',
#         'loginUin': '0',
#         'hostUin': '0',
#         'format': 'json',
#         'inCharset': 'utf8',
#         'outCharset': 'GB2312',
#         'notice': '0',
#         'platform': 'yqq.json',
#         'needNewCode': '0',
#         'cid': '205360772',
#         'reqtype': '2',
#         'biztype': '1',
#         'topid': '648242',
#         'cmd': '8',
#         'needmusiccrit': '0',  
#         'pagenum': str(i),
#         'pagesize': '25',
#         'lasthotcommentid': last,#上一页最后的id
#         'domain': 'qq.com',
#         'ct': '24',
#         'cv': '10101010'  
#         }
#         # 将参数封装为字典
#         res_suggestion = requests.get(url,params=params,headers=headers)#使用params参数确定下一页的规律，params在Header-->Query。。。。里
#         # 调用get方法，下载这个字典
#         json_suggestion = res_suggestion.json()
#         # 使用json()方法，将response对象，转为列表/字典
#         list_suggestion= json_suggestion['comment']['commentlist']
#         # 一层一层地取字典，获取歌单列表
#         for suggestion in list_suggestion:
#         # list_music是一个列表，music是它里面的元素
#             try:
#                 f.write('用户：'+suggestion['rootcommentnick'])
#                 f.write('评论：'+suggestion['rootcommentcontent']+'\n')
#             except:
#                 f.write('用户：不存在')
#                 f.write('评论：'+'评论不存在'+'\n')
#                 # 以name为键，查找歌曲名
#                 # 查找专辑名
#         last=json_suggestion['comment']['commentlist'][-1]['rootcommentid']
# #歌词
# with open('66.txt','w') as f:
#     for i in range(1,6):  
#         params = {
#         'ct': '24',
#         'qqmusic_ver': '1298',
#         'remoteplace': 'txt.yqq.top',
#         'searchid': '1',
#         'aggr': '0',
#         'catZhida': '1',
#         'lossless': '0',
#         'sem': '1',
#         't': '7',
#         'p':str(i),
#         'n': '5',
#         'w': '周杰伦',
#         '_': '1620535029344',
#         'cv': '4747474',
#         'ct': '24',
#         'format': 'json',
#         'inCharset': 'utf-8',
#         'outCharset': 'utf-8',
#         'notice': '0',
#         'platform': 'yqq.json',
#         'needNewCode': '0',
#         'uin': '0',
#         'g_tk_new_20200303': '5381',
#         'g_tk': '5381',
#         'hostUin': '0',
#         'loginUin': '0'
#         }
#         # 将参数封装为字典
#         res_lyric = requests.get(url2,params=params,headers=headers)#使用params参数确定下一页的规律，params在Header-->Query。。。。里
#         # 调用get方法，下载这个字典
#         json_lyric = res_lyric.json()
#         # 使用json()方法，将response对象，转为列表/字典
#         list_lyric= json_lyric['data']['lyric']['list']
#         # 一层一层地取字典，获取歌单列表
#         for suggestion in list_lyric:
#         # list_music是一个列表，music是它里面的元素
#             try:
#                 f.write('歌词：'+suggestion['content']+'\n')
#             except:
#                 f.write('用户：不存在')
#                 f.write('评论：'+'评论不存在'+'\n')
#                 # 以name为键，查找歌曲名
#                 # 查找专辑名

