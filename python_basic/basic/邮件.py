import smtplib
import csv
from email.mime.text import MIMEText
from email.header import Header
data=[['1048119288@qq.com'],['1146286353@qq.com']]
with open('to_addrs.csv', 'w', newline='') as f:
    writer=csv.writer(f)
    for row in data:
        writer.writerow(row)
username='1048119288@qq.com'
password='uzdifxhyewsabdcf'
text=''
with open('to_addrs.csv', 'r', newline='', encoding='utf-8-sig') as f:
    reader =csv.reader(f)
    for row in reader:
        msg=MIMEText(text,'plain','utf-8')
        msg['From']=Header('你未来的女朋友')
        msg['To']=Header('老公')
        msg['Subject']=Header('情书')
        server = smtplib.SMTP_SSL('smtp.qq.com')
        server.connect('smtp.qq.com',465)
        server.login(username,password)
        server.sendmail(username,row[0],msg.as_string())
server.quit()