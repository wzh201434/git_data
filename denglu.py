import urllib.request
import urllib.parse
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Cookie':'anonymid=jpklg08k-ycvg3z; depovince=AH; _r01_=1; JSESSIONID=abceZb6h0Rt3jbFNByGEw; ' \
              'ick_login=58dd0c66-1801-4e7f-9313-bc775783c87e; t=ee6b40065db70bbe4859621fd873d2ac3; '
             'societyguester=ee6b40065db70bbe4859621fd873d2ac3; id=969089763; xnsid=5f9de439; '
             'jebecookies=c86bdc7e-7e50-4a30-a6c2-34e608b510e5|||||; ch_id=10016; '
             'jebe_key=e8868422-c6fc-476a-8966-bc548754e952%7Cde9e5ec5ce08fee7266ef0454a6ea6de%7C1544584046981%7C1%7C1544584048382; '
             'wp_fold=0'

}
url = 'http://www.renren.com/969089763/profile'
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
with open('denglu.html','wb')as fp:
    fp.write(response.read())

