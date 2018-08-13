import urllib.request
from lxml import etree


def handle_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    return urllib.request.Request(url=url, headers=headers)


def parse_content(content, fp):
    tree = etree.HTML(content)
    # 获取每一个段子的所有信息
    odiv_list = tree.xpath('//div[@id="content-left"]/div')
    # print(len(odiv_list))
    for odiv in odiv_list:
        # 获取头像
        try:
            image_src = odiv.xpath('./div[@class="author clearfix"]/a/img/@src')[0]
        except Exception as e:
            image_src = ''
        
        # 获取用户名
        name = odiv.xpath('./div[@class="author clearfix"]//h2/text()')[0]
        # 获取年龄
        try:
            age = odiv.xpath('./div[@class="author clearfix"]/div/text()')[0]
        except Exception as e:
            age = ''
        
        # 获取内容  自己获取
        item = {
            '头像': image_src,
            '用户名': name,
            '年龄': age
        }
        fp.write(str(item) + '\n')


def main():
    fp = open('qiu.txt', 'w', encoding='utf8')
    url = 'https://www.qiushibaike.com/'
    request = handle_request(url)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf8')
    parse_content(content, fp)
    fp.close()


if __name__ == '__main__':
    main()