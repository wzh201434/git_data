import urllib.request
import urllib.parse
import os
url = 'https://tieba.baidu.com/f?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
ba_name = input('请输入要爬去的吧名：')
start_page = int(input('起始页码：'))
end_page = int(input('终止页码：'))
if not os.path.exists(ba_name):
    os.mkdir(ba_name)
for page in range(start_page,end_page+1):
    data = {
        'kw':ba_name,
        'ie':'utf-8',
        'pn':(page-1)*50
    }
    data = urllib.parse.urlencode(data)
    url_t = url+data
    request = urllib.request.Request(url=url_t,headers=headers)
    print('第%s页开始下载：'%page)
    response = urllib.request.urlopen(request)
    filename = ba_name+'_'+str(page)+'.html'
    filepath = ba_name+'/'+filename
    with open(filepath,'wb')as fp:
        fp.write(response.read())
    print('第%s页结束下载。'%page)




