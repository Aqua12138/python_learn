import time
import threading
#线程的执行先后是没有顺序的
def sing(name, num):
    for i in range(num):
        print(name, "唱歌...")
        time.sleep(1)

def dance(name, num):
    for i in range(num):
        print(name, "跳舞...")
        time.sleep(1)

if __name__ == '__main__':
    # sing()
    # dance()
    # 方法一： 设置守护
    sing_thread = threading.Thread(target=sing, args=('肖文瑜', 4), daemon=True)
    dancce_thread = threading.Thread(target=dance, kwargs={"name": '哒哒', "num": 4}, daemon=True)
    # 方法二： 设置守护
    sing_thread.setDaemon(True)
    sing_thread.start()
    dancce_thread.start()
    time.sleep(2)
    print('主线程结束了')

