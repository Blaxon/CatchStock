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
            #strip()ȥ��ǰ��ո�,split('\t')ȥ��Tab��
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
            print '�ؼ���Ϊһ���ַ���'
        return stockdata

class stockattribute(DataManage):
    def __init__(self):
        self.stock={}

    def lineformat(self,stockcode):
        '''���һ���б��б��ӵ�ԪΪÿ�������,һ���ӵ�ԪΪһ��'''
        if stockcode not in self.stock:
            self.stock[stockcode]=DataManage().searchfile(stockcode)[stockcode]
        listformat=[line.split(",") for line in self.stock[stockcode]]
        return listformat

    def colformat(self,stockcode):
        '''���һ���б��б�[0]Ϊ����,[1]Ϊ���̼�,[2]Ϊ��߼�,[3]Ϊ��ͼ�,
[4]Ϊ���̼�,[5]Ϊvolume,colformat��lineformatҪ��һ������'''
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
        '''���һ��{���ڣ����̼�}�ֵ�'''
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
        '''���һ��{����:���̼�}�ֵ�'''
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
        '''���һ��{����:����߼�}�ֵ�'''
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
        '''���һ��{����:����ͼ�}�ֵ�'''
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
        '''���һ��{����:volume}�ֵ�'''
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
