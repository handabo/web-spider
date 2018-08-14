import threading
import time


class SingThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('传递过来的参数为%s' % self.name)
        for x in range(1, 6):
            print('我喜欢唱走进新时代')
            time.sleep(1)


class DanceThread(threading.Thread):
    def run(self):
        for x in range(1, 6):
            print('你喜欢跳钢管舞')
            time.sleep(1)


def main():
    name = '迪丽热巴'
    t_sing = SingThread(name)
    t_dance = DanceThread()

    # 启动线程
    t_sing.start()
    t_dance.start()

    # 让主线程等待子线程结束之后再结束
    t_sing.join()
    t_dance.join()

    print('全部结束')


if __name__ == '__main__':
    main()