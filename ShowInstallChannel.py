#!/usr/bin/env python
#_*_ coding:utf-8 _*_

'''
作者：cloudhuan
blog：http://blog.csdn.net/cloud_huan
'''

import os,sys,re
import thread,threading
import shutil
import time

########################################################################
class CheckChannel():
    """"""
    #----------------------------------------------------------------------
    list_channel = []
    def __init__(self,apkDir = '/home/cloudhuan/桌面/tmp'):
        """Constructor"""
        self.apkDir = apkDir
    
    def check(self):
        self.listDir = os.listdir(self.apkDir)
        for apk in self.listDir:
            CheckThread(apk, self.apkDir,self.list_channel).start()
        self.pp()
            
    def pp(self):
        if len(self.list_channel) == len(self.listDir):
            print "渠道号共有这么多个:",len(self.list_channel)
            for i in self.list_channel:
                print i
        else:
            time.sleep(5)
            self.pp()
                
        
            
########################################################################
class CheckThread(threading.Thread):
    """"""
    #----------------------------------------------------------------------
    def __init__(self,apk,apkDir,list_channel):
        """Constructor"""
        threading.Thread.__init__(self)
        self.apk = apk
        self.apkDir = apkDir
        self.list_channel = list_channel
    
    def run(self):
        apk_name = os.path.splitext(self.apk)[0]
        apk_in_path = os.path.join(self.apkDir,self.apk)
        apk_out_path = os.path.join(self.apkDir,apk_name)
        cmd = 'java -jar apktool.jar d -f -s %s %s'%(apk_in_path,apk_out_path)
        os.popen(cmd)
        manifest_path = os.path.join(apk_out_path,'AndroidManifest.xml')
        if manifest_path == None:
            raise IOError
        with open(manifest_path,'r') as f:
            m_result = f.read()
        #re正则匹配的渠道key，不同apk可能不一样,这里是InstallChannel，有的是umeng_channel
        pattern = re.compile(r'<meta-data android:name="%s" android:value="(\w+)"'%'InstallChannel') 
        self.list_channel.append(pattern.findall(m_result)[0])
        shutil.rmtree(apk_out_path)

if __name__ == '__main__':
    #实例化CheckChannel对象传入路径，默认是我的测试路径，如CheckChannel('c:/user/cloudhuan/test')
    CheckChannel().check()

    