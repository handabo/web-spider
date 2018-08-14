from multiprocessing import Pool
import time
import os


def demo(name):
    print('任务的名称为%s,当前进程的id号为%s' % (name, os.getpid()))
    time.sleep(2)


def main():
    # 创建一个进程池对象
    po = Pool(5)
    # 给进程池扔任务
    lt = ['关羽', '张飞', '赵云', '马超', '黄忠', '许褚', '典韦', '张辽', '夏侯惇', '夏侯渊', '张郃']
    for name in lt:
        po.apply_async(demo, args=(name, ))
    
    # 关闭进程池，不能再向进程池中添加任务了
    po.close()
    # 让主进程等待进程池中进程全部结束之后再结束
    po.join()
    print('主进程、子进程全部结束')


if __name__ == '__main__':
    main()