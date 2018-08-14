from multiprocessing import Process
import time


name = '宋小宝'


def change():
    global name
    name = '金城武'
    print('change进程修改后的值为%s' % name)


def read():
    time.sleep(3)
    print('read进程读取的值为%s' % name)


def main():
    p1 = Process(target=change)
    p2 = Process(target=read)

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('全部结束')


if __name__ == '__main__':
    main()