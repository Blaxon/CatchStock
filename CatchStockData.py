# -*- coding: cp936 -*-
import urllib,urllib2,re,os,thread,threading,time,socket
from GetStockCode import stockname

Errorfile=[]
socket.setdefaulttimeout(40)
class stock:
    def __init__(self):
        self.stocks=stockname().readcode()
        self.pathname='StockData'
        self.Errors=[]
        
    def stockinfodown(self,stock,path):
        '''下载函数'''
        stockcode=stock[0]
        stockname=stock[1]
        stocksite='.ss' if (int(stockcode)//100000==6) else '.sz'
        url='http://table.finance.yahoo.com/table.csv?s='+stockcode+stocksite
        #print stock[0]
        filename=stockcode+'.csv'
        path=path+filename
        try:
            urllib.urlretrieve(url,path)#下载
        except urllib2.URLError,e:
            if e.code==404 or e.code==403:
                Errorfile.appende(url)
                print 'Error 404 is %s'%(url)
            else:
                self.Errors.append(url)
                print 'Error %s :download error is %s'%(e.code,url)

    def errorlog(self,path):
        '''错误处理函数,处理异常下载'''
        errors=self.Errors
        self.Errors=[]
        print '开始处理错误网页'
        for newurl in errors:
            try:
                time.sleep(5)
                urllib.urlretrieve(url,path) #这里的path是一个文件夹路径，而不是文件路径，会出错
            except urllib2.URLError,e:
                Errorfile.append([url,e.reason])
                print 'Error %s is %s'%(e.code,e.reason)
                continue

    def filecheck(self):
        smallfile=[]
        stockcode=[]
        path=os.getcwd()+'\\StockData'
        lists=os.listdir(path)
        for datafile in lists:
            filepath=path+'\\'+datafile
            length_l=os.path.getsize(filepath)
            if length_l<4096:
                #os.remove(filepath)
                smallfile.append(filepath)
                code=datafile.split(".")[0]
                stockcode.append(code)
        return smallfile,stockcode

    def stockthread(self):
        filepath=os.getcwd()+'\\'+'StockData'+'\\'
        i=0#a test uesed
        for stock in self.stocks:
            try:
                t=threading.Thread(target=self.stockinfodown,args=(stock,filepath))
                num=threading.active_count()
                if num<25:
                    t.start()
                else:
                    t.start()
                    t.join()
                i=i+1#a test uesed
                print i#a test used
            except:
                self.stockinfodown(stock,filepath)#此处有修改，path->filepath
        print 'Number of error is %s'%(len(self.Errors))
        while len(self.Errors)>0:
            print 'Number of error is %s'%(len(self.Errors))#此处有修改
            self.errorlog(filepath)#这里传值有问题，errorlog需要文件路径，而不是文件夹路径

    def stock(self):
        path=os.getcwd()+'\\'+'StockData'+'\\' #这个应该是对windows有效，macos、linux应改为'/'
        for stock in self.stocks:
            self.stockinfodown(stock,path)
            
##if __name__=='__main__':
##    s=stock()
##    s.stockthread()
##    f=file('Error.txt','w')
##    for e in Errorfile:
##        f.write(e)
##    f.close()
##    print 'Main software Finish'
    
