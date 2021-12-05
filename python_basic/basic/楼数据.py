import csv
title = input('请输入小区名称')
address = input('请输入小区地址：')
year = input('请输入小区建造年份：')
block = input('请输入楼栋号：')
unit=input('请输入单元：')
start_floor=input('请输入起始蹭数：')
end_floor=input('请输入顶层数')
floor_data={}
last_number=[]
while True:
    last_number.append(input('请输入户室尾号：'))
    distance=input('朝向是南北还是东西：')
    area=input('请输入面积：')
    floor_data[start_floor+last_number[-1]]=(distance,area)
    A=input('是否继续添加单元数? Y or N\n')
    if A=='N':
        break
with open('/Users/app/Desktop/A.csv','w',encoding='GBK') as f:
    writer=csv.writer(f)
    header = ['小区名称','地址', '建筑时间','楼栋', '单元',  '门牌', '朝向', '面积']
    writer.writerow(header)
    for i in range(int(start_floor),int(end_floor)+1):
        for j in range(len(last_number)):
            data=[title,address,year,block,unit,str(i)+last_number[j],floor_data[start_floor+last_number[j]][0],floor_data[start_floor+last_number[j]][1]]
            writer.writerow(data)
    
