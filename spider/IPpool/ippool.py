from lxml.html import etree
import threading
import requests
import re


#解析网页，并得到网页中的IP代理
def get_proxy(selector):
    
    proxies = []
 
    for each in selector.xpath("//tr[@class='odd']"):
        #ip.append(each[0])
        ip = each.xpath("./td[2]/text()")[0]
        port = each.xpath("./td[3]/text()")[0]
   

        #拼接IP地址，端口号
        proxy = ip + ":" + port
        proxies.append(proxy)
    print(len(proxies))
    test_proxies(proxies)
 
 
def thread_write_proxy(proxy):
    with open("./ip_proxy.txt", 'a+') as f:
        print("正在写入：", proxy)
        f.write(proxy + '\n')
        print("录入完成！！！")
 
 
#添加线程模式
def thread_test_proxy(proxy):
    url = "http://www.baidu.com/"
    header = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    
    try:
        response = requests.get(
            url, headers=header, proxies={"http": proxy}, timeout=1)
        if response.status_code == 200:
            print("该代理IP可用：", proxy)
            #normal_proxies.append(proxy)
            thread_write_proxy(proxy)
        else:
            print("该代理IP不可用：", proxy)
    except Exception:
        print("该代理IP无效：", proxy)
        pass
 
 
 
#验证已得到IP的可用性
def test_proxies(proxies):
    proxies = proxies
    #print("test_proxies函数开始运行。。。\n", proxies)
    for proxy in proxies:
        test = threading.Thread(target=thread_test_proxy, args=(proxy, ))
        test.start()
 
 
 
def get_html(url):
    header = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
   
    response = requests.get(
        url,
        headers=header,
    )

    for i in range(2, 100):
        selector = etree.HTML(response.text)
        get_proxy(selector)
        url = 'http://www.xicidaili.com/nn/' + str(i)
        response = requests.get(
        url,
        headers=header,
        )

def get_next_html(text):
    selector = etree.HTML(text)
    
 
if __name__ == "__main__":
 
    url = "http://www.xicidaili.com/nn/"
    get_html(url)
