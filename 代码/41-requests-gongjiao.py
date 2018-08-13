import requests
from bs4 import BeautifulSoup
import json


headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


def main():
    # 打开文件
    fp = open('成都公交.txt', 'w', encoding='utf8')
    url = 'http://chengdu.8684.cn/'
    # 解析第一个页面，得到所有的数字和字母链接
    href_list = parse_first_page(url)
    # 向数字和字母链接发送请求
    for href in href_list:
        r = requests.get(url=href, headers=headers)
        # 解析二级页面，得到所有的以4开头的所有链接
        parse_second_page(url, r.text, fp)
    
    fp.close()


def parse_second_page(url, content, fp):
    soup = BeautifulSoup(content, 'lxml')
    lt = soup.select('#con_site_1 > a')
    # 获取a链接的标题和链接
    for oa in lt:
        title = oa['title']
        href = url.rstrip('/') + oa['href']
        # 爬取每一路公交的详细信息
        parse_third_page(href, title, fp)


def parse_third_page(url, title, fp):
    print('正在爬取--%s......' % title)
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    # 获取公交名字
    name = soup.find('h1').string
    # 获取运行时间
    runtime = soup.select('.bus_i_t4')[0].string.lstrip('运行时间：')
    # 获取票价信息
    price = soup.select('.bus_i_t4')[1].string.lstrip('票价信息：')
    # 获取公交公司
    company = soup.select('.bus_i_t4 > a')[0].string
    # 更新时间
    gxsj = soup.select('.bus_i_t4')[-1].string
    # 获取公里数
    # length = soup.select('.bus_label_t2').string.strip('全程公里。')
    # 获取上行和下行总站数
    up_total = soup.select('.bus_line_no')[0].string
    # 上行站牌
    div0 = soup.select('.bus_site_layer')[0]
    up_href_list = div0.select('div > a')
    up_name_list = []
    for oa in up_href_list:
        up_name_list.append(oa.string)
    
    try:
        down_total = soup.select('.bus_line_no')[1].string
        # 下行站牌
        div1 = soup.select('.bus_site_layer')[1]
        down_href_list = div1.select('div > a')
        down_name_list = []
        for oa in down_href_list:
            down_name_list.append(oa.string)
    except Exception as e:
        down_total = '亲-没有下行'
        down_name_list = '亲-这是环形'

    item = {
        '公交名称': name,
        '运行时间': runtime,
        '票价信息': price,
        '公交信息': company,
        '更新时间': gxsj,
        # '公里数': length,
        '上行站牌数': up_total,
        '上行站牌': up_name_list,
        '下行站牌数': down_total,
        '下行站牌': down_name_list,
    }
    string = json.dumps(item, ensure_ascii=False)
    fp.write(string + '\n')
    print('结束爬取--%s' % title)


def parse_first_page(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    # 得到所有数字开头链接
    number_list = soup.select('.bus_kt_r1 > a')
    # print(len(number_list))
    # 得到所有以字母开头的链接
    char_list = soup.select('.bus_kt_r2 > a')
    lt = number_list + char_list
    # 遍历得到所有的href属性
    href_list = []
    for oa in lt:
        href = url.rstrip('/') + oa['href']
        href_list.append(href)
    return href_list


if __name__ == '__main__':
    main()