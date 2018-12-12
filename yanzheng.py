import urllib.request
import urllib.parse
handler = urllib.request.ProxyHandler({'http':'113.200.56.13:8010'})
opener = urllib.request.build_opener(handler)
url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
request = urllib.request.Request(url,headers=headers)
response = opener.open(request)
with open('ip.html','wb')as fp:
    fp.write(response.read())
