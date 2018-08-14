import threading
import time


def sing(dudu):
    print('传递过来的参数为%s' % dudu)
    print('sing线程的名字为%s' % threading.current_thread().name)
    for x in range(1, 6):
        print('我喜欢唱走进新时代')
        time.sleep(1)


def dance():
    print('dance线程的名字为%s' % threading.current_thread().name)
    for x in range(1, 6):
        print('你喜欢跳钢管舞')
        time.sleep(1)


# 一个主线程，两个子线程
def main():
    lala = '赵丽颖'
    print('主线程的名字为%s' % threading.current_thread().name)
    t_sing = threading.Thread(target=sing, name='唱歌', args=(lala,))
    t_dance = threading.Thread(target=dance)

    # 启动线程
    t_sing.start()
    t_dance.start()

    # 让主线程等待子线程结束之后再结束
    t_sing.join()
    t_dance.join()

    print('全部结束')


if __name__ == '__main__':
    main()