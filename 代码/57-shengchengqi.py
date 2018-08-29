# baby = '清明时节雨纷纷,路上行人欲断魂,借问酒家何处有,牧童遥指杏花村'

# print(eval('baby'))

def demo():
    lt = []
    for x in range(1, 101):
        lt.append(x)
    return lt

# 生成器，保存数据的生成方式，你给他要，他给你生成一个
def test():
    for x in range(1, 11):
        yield x
        yield '王力宏'
    yield 'she'

g = test()
print(g)
for x in g:
    print(x)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))