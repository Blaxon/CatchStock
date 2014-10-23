import urllib2,re

class stockname:
    def __init__(self):
        self.txtname='stockcode'
        
    def readcode(self):
        page=urllib2.urlopen('http://bbs.10jqka.com.cn/codelist.html')
        pagedata=page.read()
        page.close()
        href=re.compile('<a href="http://bbs.10jqka.com.cn/[sf][zhu],(.*?),1" target="_blank" title="(.*?)">')
        addresslist=re.findall(href,pagedata)
        return addresslist
    
    def writecode(self):
        stockcode=open(self.txtname+'.txt','wt')
        for stockname in self.readcode():
            w=str(stockname[0])+':'+str(stockname[1])
            stockcode.write(w)
            stockcode.write('\n')
        stockcode.close

