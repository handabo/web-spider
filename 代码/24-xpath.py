from lxml import etree

# 生成对象
tree = etree.parse('test.html')
# print(tree)

# ret = tree.xpath('//a[@class="lala"]')
# ret = tree.xpath('//div[@class="tang"]/ul/li/b[2]')
# ret = tree.xpath('//a[@id="dudu"]/text()')
# ret = tree.xpath('//a[@id="dudu"]/@href')
# print(ret)

# 获取标签里面还有标签的内容可以使用如下两种方式
# ret = tree.xpath('//div[@class="hero"]//text()')
# string = ''.join(ret).replace('\n', '').replace(' ', '')
# print(string)

# 先找到div这个对象
# odiv = tree.xpath('//div[@class="hero"]')[0]
# string = odiv.xpath('string(.)').replace('\n', '').replace(' ', '')
# print(string)

# ret = tree.xpath('//b[starts-with(@class,"mei")]/text()')
# ret = tree.xpath('//b[contains(text(), "一")]/text()')
# print(ret)