from multiprocessing import Process
import time


class SingProcess(Process):
    def __init__(self, name):
        # 手动调用父类的构造方法
        super().__init__()
        self.name = name

    # 进程启动之后，默认执行这个函数 
    def run(self):
        print('传递过来的参数为%s' % self.name)
        for x in range(1, 6):
            print('我在唱女儿情')
            time.sleep(1)


class DanceProcess(Process):
    def run(self):
        for x in range(1, 6):
            print('我在跳广场舞')
            time.sleep(1)


def main():
    name = '柳岩'
    ps = SingProcess(name)
    pd = DanceProcess()
    ps.start()
    pd.start()
    ps.join()
    pd.join()
    print('主进程, 子进程全部结束')


if __name__ == '__main__':
    main()