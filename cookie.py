import urllib,urllib2
import cookielib

url = "http://www.baidu.com"
data = {"name":"test"}
info = urllib.urlencode(data)
head = {"Use-Agent":""}
req = urllib2.Request(url,info,head)
#resp = urllib2.urlopen(req)
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
resp = opener.open(req)
for i in cookie:
    print "name is : %s"%i.name
    print "value is : %s"%i.value