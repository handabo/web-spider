from multiprocessing import Process
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
    p1 = Process(target=demo, args=('change', ))
    p2 = Process(target=demo, args=('read', ))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('全部结束')


if __name__ == '__main__':
    main()