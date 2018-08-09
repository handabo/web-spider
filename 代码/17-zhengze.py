import re
'''
string = 'i love you very love much'
pattern = re.compile(r'love')
匹配失败返回None
ret = pattern.match(string)

ret = pattern.search(string)
ret = pattern.findall(string)

print(ret)
得到匹配的内容, 只匹配一个，成功立马结束
print(ret.group())
print(ret.span())
'''


'''
# (1)子模式
string = '哈哈<div><span>天青色等烟雨,而我在等你</span></div>嘻嘻'
pattern = re.compile(r'<(\w+)><(\w+)>.*</\2></\1>')
# pattern = re.compile(r'<(?P<goudan>\w+)><(?P<maodan>\w+)>.*</(?P=maodan)></(?P=goudan)>')

ret = pattern.search(string)
print(ret.group())
print(ret.group(1))
print(ret.group(2))
'''

'''
# (2)贪婪模式
string = '<div>啦啦啦啦啦啦，我是卖报的小行家</div></div></div></div>'
pattern = re.compile(r'<div>(.*?)</div>')
ret = pattern.search(string)

print(ret.group(1))
'''

'''
# (3)忽略大小写
string = 'love is a forever topic'
pattern = re.compile(r'LOVE', re.I)

ret = pattern.search(string)

print(ret.group())
'''
"""
# (4)多行模式
string = '''细思极恐
你的对手在看书
你的敌人在磨刀
你的闺蜜在减肥
隔壁老王在炼腰
'''
pattern = re.compile(r'^你的', re.M)
ret = pattern.search(string)

print(ret.group())
"""

# (5)单行模式
string = '''<div>沁园春-雪
北国风光，千里冰封，万里雪飘
望长城内外，惟余莽莽
大河上下，顿失滔滔
</div>'''
pattern = re.compile(r'<div>(.*?)</div>', re.S)
ret = pattern.search(string)
print(ret.group(1))