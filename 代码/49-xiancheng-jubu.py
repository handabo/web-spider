from threading import Thread
import time


def demo(lala):
    name = '朱茵'
    if lala == 'change':
        name = '张敏'
        print('change修改后的值为%s' % name)
    else:
        time.sleep(3)
        print('read进来读取name的值为%s' % name)


def main():
    t1 = Thread(target=demo, args=('change', ))
    t2 = Thread(target=demo, args=('read', ))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('全部结束')


if __name__ == '__main__':
    main()