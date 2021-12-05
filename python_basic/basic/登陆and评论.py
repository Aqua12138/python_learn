import requests
link_1='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
data_1={
    'log': 'spiderman',
    'pwd': 'crawler334566',
'rememberme': 'forever',
'wp-submit': '登录',
'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
'testcookie': '1'
}
login_in = requests.post(url=link_1,headers=headers,data=data_1)
cookies=login_in.cookies
link_2='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
data_2={
    'comment': '666',
'submit': '发表评论',
'comment_post_ID': '24',
'comment_parent': '0'
}
comment=requests.post(url=link_2,headers=headers,data=data_2,cookies=cookies)
print(comment.status_code)