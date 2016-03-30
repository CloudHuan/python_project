#_*_coding: utf-8 _*_

from pyquery import PyQuery as pq
import urllib2

html = u'''<div id="info">
<span><span class='pl'>导演</span>: <a href="/celebrity/1047989/" rel="v:directedBy">汤姆·提克威</a> / <a href="/celebrity/1161012/" rel="v:directedBy">拉娜·沃卓斯基</a> / <a href="/celebrity/1013899/" rel="v:directedBy">安迪·沃卓斯基</a></span><br/>
<span><span class='pl'>编剧</span>: <a href="/celebrity/1047989/">汤姆·提克威</a> / <a href="/celebrity/1013899/">安迪·沃卓斯基</a> / <a href="/celebrity/1161012/">拉娜·沃卓斯基</a></span><br/>
<span><span class='pl'>主演</span>: <a href="/celebrity/1054450/" rel="v:starring">汤姆·汉克斯</a> / <a href="/celebrity/1054415/" rel="v:starring">哈莉·贝瑞</a> / <a href="/celebrity/1019049/" rel="v:starring">吉姆·布劳德本特</a> / <a href="/celebrity/1040994/" rel="v:starring">雨果·维文</a> / <a href="/celebrity/1053559/" rel="v:starring">吉姆·斯特吉斯</a> / <a href="/celebrity/1057004/" rel="v:starring">裴斗娜</a> / <a href="/celebrity/1025149/" rel="v:starring">本·卫肖</a> / <a href="/celebrity/1049713/" rel="v:starring">詹姆斯·达西</a> / <a href="/celebrity/1027798/" rel="v:starring">周迅</a> / <a href="/celebrity/1019012/" rel="v:starring">凯斯·大卫</a> / <a href="/celebrity/1201851/" rel="v:starring">大卫·吉雅西</a> / <a href="/celebrity/1054392/" rel="v:starring">苏珊·萨兰登</a> / <a href="/celebrity/1003493/" rel="v:starring">休·格兰特</a></span><br/>
<span class="pl">类型:</span> <span property="v:genre">剧情</span> / <span property="v:genre">科幻</span> / <span property="v:genre">悬疑</span><br/>
<span class="pl">官方网站:</span> <a href="http://cloudatlas.warnerbros.com" rel="nofollow" target="_blank">cloudatlas.warnerbros.com</a><br/>
<span class="pl">制片国家/地区:</span> 德国 / 美国 / 香港 / 新加坡<br/>
<span class="pl">语言:</span> 英语<br/>
<span class="pl">上映日期:</span> <span property="v:initialReleaseDate" content="2013-01-31(中国大陆)">2013-01-31(中国大陆)</span> / <span property="v:initialReleaseDate" content="2012-10-26(美国)">2012-10-26(美国)</span><br/>
<span class="pl">片长:</span> <span property="v:runtime" content="134">134分钟(中国大陆)</span> / 172分钟(美国)<br/>
<span class="pl">IMDb链接:</span> <a href="http://www.imdb.com/title/tt1371111" target="_blank" rel="nofollow">tt1371111</a><br>
<span class="pl">官方小站:</span>
<a href="http://site.douban.com/202494/" target="_blank">电影《云图》</a>
</div>'''

html2='''
<tr height=\"30\" > <td align=\"center\"><a href=\"http://yunvs.com/600401\" target=\"_blank\">600401</a></td>
        <td align=\"center\"><a href=\"http://yunvs.com/600401\" target=\"_blank\">海润光伏</a></td>
        <td align=\"center\">17876.8</td>
        <td align=\"center\">2005.74</td>
        <td align=\"center\"><font color=\"#C00\"><b>+791.28%</b></font></td>
        <td align=\"left\"><a href=\"http://yunvs.com/theme/t640.html\" target=\"_blank\">光伏</a>&nbsp;&nbsp;<a href=\"http://yunvs.com/theme/t323.html\" target=\"_blank\">太阳能</a>&nbsp;&nbsp;<a href=\"http://yunvs.com/theme/t225.html\" target=\"_blank\">阶梯电价受益</a>&nbsp;&nbsp;<a href=\"http://yunvs.com/theme/t105.html\" target=\"_blank\">多晶硅</a>&nbsp;&nbsp;<a href=\"http://yunvs.com/theme/t285.html\" target=\"_blank\">券商(龙头)</a>&nbsp;&nbsp;<a href=\"http://yunvs.com/theme/t230.html\" target=\"_blank\">金太阳工程</a>&nbsp;&nbsp;</td>
    </tr>'''
#()里面输入匹配条件，默认是tag，或者.代表class #代表id 最后.text()输出文本
doc = pq('http://yunvs.com/list/mai_1.html')
doc_0 = doc('tr')
for i in doc_0:
    id = pq(i).find('td').eq(0).text()
    name = pq(i).find('td').eq(1).text()
    type = pq(i).find('td').eq(5).text()
    print id,name,type
    
doc = pq('http://yunvs.com/list/insidetrade_1.html')
doc0 = doc('tr')
for i in doc0:
    doc1 = pq(i).find('td')
    for j in doc1:
        print pq(j).text()