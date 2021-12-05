import multiprocessing
import time
import os
def dance(num, name):
    #获取当前进程的编号
    print('dance进程的编号是:', os.getpid())
    print('通过子进程获取父进程的编号：', os.getppid())
    for i in range(num):
        print('lets dance')
        print(name)
        time.sleep(0.5)
def sing(num):
    print('sing进程的编号是:', os.getpid())
    for i in range(num):
        print('lets sing')
        time.sleep(0.5)

def main():
    print('主进程编号:', os.getpid())
    sing_process = multiprocessing.Process(target=sing, args=(5,))#注意是sing 不是sing() arg表示以元组方式传参
    dance_process = multiprocessing.Process(target=dance, kwargs={"num": 4, "name": "小红"}) # kwarg表示以字典方式传参
    dance_process.start()
    sing_process.start()
    time.sleep(1)
    # 主进程会等待子进程结束后才会结束
    print("主进程执行完了！")

if __name__ == '__main__':
    # sing()
    # dance()
    main()
