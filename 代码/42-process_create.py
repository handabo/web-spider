from multiprocessing import Process
import time
import os


def sing(name):
    print('sing接受过来的明星为%s' % name)
    print('sing的id号为%s' % os.getpid())
    print('sing的父进程id为%s' % os.getppid())
    for x in range(1, 6):
        print('我在唱青藏高原')
        time.sleep(1)


def dance():
    print('dance的id号为%s' % os.getpid())
    print('dance的父进程id为%s' % os.getppid())
    for x in range(1, 6):
        print('我在跳拉丁舞')
        time.sleep(1)


# 一个主进程，用来负责创建子进程的，然后一个唱歌子进程，一个跳舞子进程
def main():
    # 主进程可以给子进程传递参数
    name = '高圆圆'
    print('主进程的id号为%s' % os.getpid())
    # 创建进程
    p_sing = Process(target=sing, args=(name,))
    p_dance = Process(target=dance)

    # 启动进程
    p_sing.start()
    p_dance.start()

    # 需要让主进程等待子进程结束之后再结束
    p_sing.join()
    p_dance.join()

    print('主进程、子进程全部运行结束')


if __name__ == '__main__':
    main()