#!/use/bin/env python
#_*_coding:utf-8_*_
'''
author： cloudhuan
说明：cd到对应目录，自动获取 当前目录/2016xxxx/xxx.txt文件，解析对应字段，输出当前目录下xls文件
'''
import os
import sys
import re
import urllib2
import json
import thread,threading
import xlwt
import time

########################################################################
class TogicLog():
    """"""   
    result_list = []
    thread_list = []
    class ParseThread(threading.Thread):
        #定义内部线程类，构造函数传入包含有很多path的list
        def __init__(self,data_list,result_list):
            threading.Thread.__init__(self)
            self.data_list = data_list
            self.result_list = result_list
            
        def run(self):
            for i in self.data_list:
                self.startParse(i)
                
    
        #传入url(或者文件名path+fileName)，返回设备信息list
        def startParse(self,url = 'http://logcat1.tvos.com/logs/20160317/EBOX%20E12~version[88]~4177000000e04e10474d32bbb62689000000000000000000~1458228281773~EBOX%20E12_4.2.2_2016.03.17_23:24_1.txt'):
            if 'http' in url:
                req = urllib2.Request(url,headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)'})
                resp = urllib2.urlopen(req).read()
            else:
                with open(url,'r+') as f:
                    resp = f.read()           
                    #pattern = re.compile(u'PT=[\w|\d|-|.]+') 
                    #info_all = pattern.findall(resp)
                    #j_result = json.loads(info)
                    #print j_result['qua']
            try:
                result_MD = re.findall(u'&MD=([\w|\d|.|*|\s|]+)',resp)[0]
                result_VN = re.findall(u'&VN=([\d|.|\s]+)',resp)[0]
                result_BD = re.findall(u'&BD=([\w|\d|.|\s]+)',resp)[0]
                result_RL = re.findall(u'&RL=([\w|\d|.|*]+)',resp)[0]            
            except:
                print '读入的格式不规范'
                return
            print [result_MD,result_VN,result_BD,result_RL]
            self.result_list.append([result_MD,result_VN,result_BD,result_RL])
            
            
    #递归列出当前文件夹下所有.txt文件20160318/xxx.txt
    def searchFile(self,path=os.path.abspath(os.curdir)):
        """"""
        l_dir = os.listdir(path)
        l_dir = map(lambda x:os.path.join(path,x),l_dir)  #add path to list file
        l_dir = filter(lambda x:os.path.isdir(x),l_dir)  #check is dir
        for txtFile in l_dir:
            ll_dir = os.listdir(txtFile)
            ll_dir = filter(lambda x:os.path.splitext(x)[1] == '.txt',ll_dir)
            ll_dir = map(lambda x:os.path.join(txtFile,x),ll_dir)
            t = self.ParseThread(ll_dir ,self.result_list)
            t.start()
            self.thread_list.append(t)
        for t in self.thread_list:
            t.join()
        #self.outXLS(self.staticInfo(self.result_list))  
        #某些服务器不支持xlswt模块，改用直接print输出
        self.printInfo(self.staticInfo(self.result_list))
    
    #----------------------------------------------------------------------
    def staticInfo(self,result_list):
        """"""
        temp = []
        for i in result_list:
            if i in temp:
                continue
            temp.append(i)
        print temp
        return temp

    #----------------------------------------------------------------------
    def outXLS(self,out_list):
        """"""
        wb = xlwt.Workbook()
        table = wb.add_sheet('togic')  
        table.write(0,0,u'机型')
        table.write(0,1,u'系统版本')
        table.write(0,2,u'处理器') 
        table.write(0,3,u'分辨率')        
        c_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        po = 1
        for p in out_list:
            table.write(po,0,p[0])
            table.write(po,1,p[1])
            table.write(po,2,p[2])
            table.write(po,3,p[3])
            po += 1
        wb.save(os.getcwd()+'/'+'togic-'+c_time+'.xls')
        
    def printInfo(self,out_list):
        print '\n','\n','结果是：','\n'
        for p in out_list:
            print p
        
if __name__ == '__main__':         
   TogicLog().searchFile()