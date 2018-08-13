import requests

post_url = 'https://cn.bing.com/ttranslationlookup?&IG=ECFF4CD98C524F66B5D55062F0E9D9E4&IID=translator.5036.14'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
data = {
    'from': 'zh-CHS',
    'to': 'en',
    'text': '饺子',
}
r = requests.post(url=post_url, headers=headers, data=data)
print(r.text)