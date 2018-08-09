import urllib.request

url = 'http://www.renren.com/960481378/profile'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
	'Cookie': 'anonymid=jkl96t9i-7jfkjc; depovince=SC; _r01_=1; _de=F872F5698F7602B30ADE65415FC01940; ln_uact=17701256561; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=89a1a125-709a-4912-aa70-cbaf2eddd932%7C86ba94a3b75a9848502e25ac92562959%7C1533740001336%7C1%7C1533740008302; jebecookies=f91c2331-f0e2-4c9a-a936-3299112bbed6|||||; JSESSIONID=abcEmpXxJ_WYs8adJICuw; ick_login=a3456fda-f4c3-4dde-98b7-7994763bb807; p=e456fef62e5fb2a7971b6bb34af6b17d8; first_login_flag=1; t=01e2ec7768631eae78816a83379f3f508; societyguester=01e2ec7768631eae78816a83379f3f508; id=960481378; xnsid=e374bf01; ver=7.0; loginfrom=null; wp_fold=0',
}
request = urllib.request.Request(url=url, headers=headers)

r = urllib.request.urlopen(request)

with open('renren.html', 'wb') as fp:
	fp.write(r.read())