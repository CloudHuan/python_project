# _*_ coding:utf-8 _*_

from pyquery import PyQuery as pq
import urllib2

t = []
d = []
#csdn不让直接解析，会403,所以伪造了http请求头
head_req = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)'}
req = urllib2.Request("http://blog.csdn.net/cloud_huan",headers=head_req)
result = urllib2.urlopen(req).read()
doc = pq(result)
doc_title = doc('.article_title')
for i in doc_title:
    title = pq(i).text()
    t.append(title)
doc_des = doc('.article_description')
for i in doc_des:
    des = pq(i).text()
    d.append(des)
for i in range(0,len(t)):
    print t[i],'---',d[i]
    print '*********************'
