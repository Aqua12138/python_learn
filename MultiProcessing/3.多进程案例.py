#多进程高并发拷贝器
import os
import multiprocessing

#拷贝函数
def copy(file_name, source_dir, dest_dir):
    # 1. 拼接源文件路径和目标文件路径
    source_path = source_dir + '/' + file_name
    dest_path = dest_dir + '/' + file_name
    # 2. 打开源文件和目标文件
    #读源文件
    with open(source_path, "rb") as source_file:
        #写目标文件
        with open(dest_path, "wb") as dest_file:
            # 3. 循环读取源文件和目标路径
            while True:
                data = source_file.read(1024)#每次读取1024b字节的数据 1k
                if data:
                    dest_file.write(data)
                else:
                    break
if __name__ == '__main__':
    # 1.目标文件夹是否存在，存在就创建，如果不存在就创建
    # 1.1定义源文件夹的所在的路径、目标文件夹所在的路径
    source_dir = '/home/zhx/文档/pokemon/bulbasaur'
    dest_dir = "/home/zhx/桌面/pokemon_test"

    # 1.2创建目标文件夹
    try:
        os.mkdir(dest_dir)
    except:
        print("目标文件夹已经存在")

    # 2读取拷贝文件的所有目录列表
    file_list = os.listdir(source_dir)

    # 3.遍历每一个文件，定义一个函数，专门实现文件的拷贝
    for file_name in file_list:
        # copy(file_name, source_dir, dest_dir)
        # 4.采用多进程实现多任务，弯沉高拷贝高并发拷贝
        sub_process = multiprocessing.Process(target=copy,
                                              args=(file_name,
                                                    source_dir,
                                                    dest_dir))
        sub_process.start()
