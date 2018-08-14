import threading
from threading import Lock


# 通过加锁机制解决线程安全问题
count = 100
lock = Lock()


def test(n):
    global count
    for x in range(1, 1000000):
        lock.acquire()    # 加锁
        count += n
        count -= n
        lock.release()    # 解锁
    print('%s线程--运行结束之后count的值为%s' % (threading.current_thread().name, count))


def main():
    t1 = threading.Thread(target=test, args=(3, ))
    t2 = threading.Thread(target=test, args=(5, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('主线程读取count的值为%s' % count)
    print('全部结束')


if __name__ == '__main__':
    main()