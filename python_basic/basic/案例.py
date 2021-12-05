# 连续刷新
# import time
# for t in range(5,0,-1):   #range(起始位，终止位，步长)
#     info = '请专注任务，还要保持专注 ' + str(t) + ' 秒哦！'
#     print(info,end='')    #end=''用来表示最后的\n符号改成空，因为变成了空，所以在下一个\n出现前都不会出现结果
#     print("\b"*(len(info)*2),end='',flush=True)   #\b表示在该行处往前一个字节 #flush=true表示实时显示，避免了end=''不显示的弊端
#     time.sleep(1)

#字符拼接
# a=['d','o','g']
# b=','
# print(b.join(a))
# c='-'
# print(c.join(a))

#滚动屏幕
# import os, time
# def main():  # 用函数封装，可复用性会高一些（可在其他的.py文件里调用该函数。）
#     content = ' 风变编程，陪你一起学Python '  # 广告词可自定义。
#     while True:
#         os.system('clear')  # 完成清屏：清屏和打印结合起来，形成滚动效果。
#         print(content)
#         content = content[1:] + content[0]  # 这行代码相当于：将字符串中第一个元素移到了最后一个。
#         time.sleep(0.25)  # 你可以改下时间，体会“循环周期”和“滚动速度”之间的关联。
# if __name__ == '__main__':  # 类里面学到的检测方法，在函数中其实也可以用。
#     main()




