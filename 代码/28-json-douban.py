from bs4 import BeautifulSoup
import urllib.request
from lxml import etree
import json

'''
def main():
    url = 'https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    }
    request = urllib.request.Request(url=url, headers=headers)
    content = urllib.request.urlopen(request).read().decode('utf8')
    tree = etree.HTML(content)
    odiv_list = tree.xpath('//div[starts-with(@class,"movie-list-item")]')
    print(odiv_list)
    print(len(odiv_list))
'''


def main():
    fp = open('movie.json', 'w', encoding='utf8')
    url = 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=0&limit=20'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    content = urllib.request.urlopen(request).read().decode('utf8')

    # print(content)
    # 将json格式字符串转化为python对象
    lt = json.loads(content)
    # 遍历这个列表，依次获取每一个电影的详细信息
    lala = []
    for obj in lt:
        # 获取海报
        post = obj['cover_url']
        # 电影名字
        name = obj['title']
        # 评分
        score = obj['score']
        # 评论人数
        count = obj['vote_count']
        item = {
            '海报': post,
            '电影': name,
            '评分': score,
            '品论人数': count
        }
        lala.append(item)
        # print(obj)
        # exit()
    string = json.dumps(lala, ensure_ascii=False)
    fp.write(string)
    fp.close()


if __name__ == '__main__':
    main()