from queue import Queue

# 创建一个队列, 可以指定队列的长度，如果不写长度，默认无限长
q = Queue(5)

print(q.full())   # 队列是否满
print(q.empty())  # 队列是否空
print(q.qsize())  # 队列的元素的个数

# 向队列中添加元素
q.put('库里')
q.put('乔丹')
q.put('韦德')
print(q.full())
print(q.empty())
print(q.qsize())
q.put('字母哥')
q.put('恩比德')
# q.put('米切尔', False)
# q.put('米切尔', True, 5)
print(q.full())
print(q.empty())
print(q.qsize())

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
# print(q.get(False))
print(q.get(True, 3))