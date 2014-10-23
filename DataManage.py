# -*- coding: cp936 -*-
import os,types
class DataManage:
    def __init__(self):
        self.csvfiles=[]
        
    def dataread(self,csvfile):
        files=file(csvfile,'r')
        content=files.read()
        files.close()
        for num,line in enumerate(content.split('\n')):
            #strip()去掉前后空格,split('\t')去掉Tab键
            data=[field for field in line.strip().split('\t')]
        return data
    
    def searchfile(self,stockcode):
        stockdata={}
        if type(stockcode) is types.StringType:
            Maincatalog=os.listdir(os.getcwd())
            filename=stockcode+'.csv'
            if 'StockData' in Maincatalog:
                datapath=os.getcwd()+'\\StockData'
                subcatalog=os.listdir(datapath)
                print filename
                if filename in subcatalog:
                    stockdata[stockcode]=self.dataread(datapath+'\\'+filename)
                    print 'alread read %s data'%(filename)
                else:
                    print 'can\'t find file'
        else:
            print '关键词为一个字符串'
        return stockdata

class stockattribute(DataManage):
    def __init__(self):
        self.stock={}

    def lineformat(self,stockcode):
        '''输出一个列表，列表子单元为每天的数据,一个子单元为一天'''
        if stockcode not in self.stock:
            self.stock[stockcode]=DataManage().searchfile(stockcode)[stockcode]
        listformat=[line.split(",") for line in self.stock[stockcode]]
        return listformat

    def colformat(self,stockcode):
        '''输出一个列表，列表[0]为日期,[1]为开盘价,[2]为最高价,[3]为最低价,
[4]为收盘价,[5]为volume,colformat较lineformat要少一天数据'''
        date=[]
        openprice=[]
        highprice=[]
        lowprice=[]
        closeprice=[]
        volume=[]
        if stockcode not in self.stock:
            self.stock[stockcode]=DataManage().searchfile(stockcode)[stockcode]
        for num in range(len(self.stock[stockcode])-1):
            line=self.stock[stockcode][num]
            date.append(line.split(",")[0])
            openprice.append(line.split(",")[1])
            highprice.append(line.split(",")[2])
            lowprice.append(line.split(",")[3])
            closeprice.append(line.split(",")[4])
            volume.append(line.split(",")[5])
        return [date,openprice,highprice,lowprice,closeprice,volume]
    
    def openprice(self,stockcode):
        '''输出一个{日期：开盘价}字典'''
        date=[]
        openprice=[]
        if stockcode not in self.stock:
            self.stock[stockcode]=DataManage().searchfile(stockcode)[stockcode]
        for line in self.stock[stockcode]:
            date.append(line.split(",")[0])
            openprice.append(line.split(",")[1])
        price=dict(zip(date,openprice))
        return price

    def closeprice(self,stockcode):
        '''输出一个{日期:收盘价}字典'''
        date=[]
        closeprice=[]
        if stockcode not in self.stock:
            self.stock[stockcode]=DataManage().searchfile(stockcode)[stockcode]
        for num in range(len(self.stock[stockcode])-1):
            line=self.stock[stockcode][num]
            date.append(line.split(",")[0])
            closeprice.append(line.split(",")[4])
        price=dict(zip(date,closeprice))
        return price

    def highprice(self,stockcode):
        '''输出一个{日期:日最高价}字典'''
        date=[]
        highprice=[]
        if stockcode not in self.stock:
            self.stock[stockcode]=DataManage().searchfile(stockcode)[stockcode]
        for num in range(len(self.stock[stockcode])-1):
            line=self.stock[stockcode][num]
            date.append(line.split(",")[0])
            highprice.append(line.split(",")[2])
        price=dict(zip(date,highprice))
        return price

    def lowprice(self,stockcode):
        '''输出一个{日期:日最低价}字典'''
        date=[]
        lowprice=[]
        if stockcode not in self.stock:
            self.stock[stockcode]=DataManage().searchfile(stockcode)[stockcode]
        for num in range(len(self.stock[stockcode])-1):
            line=self.stock[stockcode][num]
            date.append(line.split(",")[0])
            lowprice.append(line.split(",")[3])
        price=dict(zip(date,lowprice))
        return price

    def volume(self,stockcode):
        '''输出一个{日期:volume}字典'''
        date=[]
        volume=[]
        if stockcode not in self.stock:
            self.stock[stockcode]=DataManage().searchfile(stockcode)[stockcode]
        for num in range(len(self.stock[stockcode])-1):
            line=self.stock[stockcode][num]
            date.append(line.split(",")[0])
            volume.append(line.split(",")[5])
        price=dict(zip(date,volume))
        return price
s=stockattribute()
print s.lineformat('000023')
