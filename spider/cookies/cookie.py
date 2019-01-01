
import requests
from http import cookiejar

if __name__ == '__main__':
    cookies = 'UM_distinctid=16740c3cf260-0b7431f9707519-3f674604-144000-16740c3cf287cc; \
    SINAGLOBAL=9017464686831.336.1542979833932; UOR=www.baidu.com,vdisk.weibo.com,www.baidu.com; \
    un=18223144116; wvr=6; login_sid_t=e29196eb77fc372373e984e6df785882; cross_origin_proto=SSL;\
    _s_tentry=passport.weibo.com; Apache=3590457592288.101.1545402553806; \
    ULV=1545402553811:5:3:2:3590457592288.101.1545402553806:1545233306050; \
    SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhRRVQGOy8gaVsud0z9DDmg5JpX5K2hUgL.FozEShBp1K5RSKM2dJLoIfQLxKMLBK.LBoMLxKBLB.2LB.2LxK-LB--LBoqLxKML1-2L1hBLxK-LB-BLBK.LxK-LB-BL1K5LxKqL1-zLBoBLxKnLBKqL1h2LxKqL12zLB.eLxKqL1K5L12qt;\
     ALF=1576938582; SSOLoginState=1545402583; \
     SCF=AlcmXKa-gHYLTwJU5hsBGZRqp4eebYjpmmw4_yNi0DxxUgHdiYUzcJiUnfjVeJFY3Zg4Z7vdJ5q3qn-aQ_lIz8E.;\
      SUB=_2A25xGIiIDeRhGeRM71YQ-S7EzjuIHXVSb_1ArDV8PUNbmtAKLUbjkW9NU_ZEqEj9AIF6LOKihTSzxqnxoVQoi-6Y; \
      SUHB=0M2EAeC1GG5ADx'

    jar = requests.cookies.RequestsCookieJar()
    header = {}
   
"""
 #设置保存cookie的文件，同级目录下的cookie.txt
    filename = 'cookie.txt'
    #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookiejar.MozillaCookieJar(filename)
    #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler=request.HTTPCookieProcessor(cookie)
    #通过CookieHandler创建opener
    opener = request.build_opener(handler)
    #此处的open方法打开网页
    response = opener.open('https://weibo.com/u/2244190857/home?wvr=5&lf=reg')
    #保存cookie到文件
    cookie.save(ignore_discard=True, ignore_expires=True)
"""
