from threading import Thread
import time


name = '宋小宝'


def change():
    global name
    name = '金城武'
    print('change线程修改后的值为%s' % name)


def read():
    time.sleep(3)
    print('read线程读取的值为%s' % name)


def main():
    t1 = Thread(target=change)
    t2 = Thread(target=read)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('全部结束')


if __name__ == '__main__':
    main()