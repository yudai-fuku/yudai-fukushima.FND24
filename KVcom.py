import time
from socket import *
import struct
import datetime
import csv
import os

cyrrent_file_path = os.path.abspath(__file__) #本プログラムのパスを取得
script_directory = os.path.dirname(cyrrent_file_path) #本プログラムのディレクトリ取得
listFilePath = script_directory + "/ListFile/ListFilefuku.csv" #リストファイルのパス



BUFSIZE = 1024

def ReadListFile(listFilePath):
    #print(listFilePath)
    listline = 0 #リストファイルの行数カウント初期化

    #リスト生成
    listA = [] #Listfile Header
    listB = [] #Listfile IP
    #listC = [] #Listfile Port
    #listD = [] #Listfile Device
    #listE = [] #Listfile DataType
    #listF = [] #Listfile Code1
    #listG = [] #Listfile Code2
    #listH = [] #Listfile Code3
    #listI = [] #Listfile Code4
    #listJ = [] #Listfile Bit
    #listK = [] #Listfile Scaling x
    #listL = [] #Listfile Scaling b
    #listM = [] #Listfile Scaling .
    
    #csvオープン
    with open(listFilePath, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        #列ごとにリストに格納
        for row in csv_reader:
            listA.append(row[0])
            listB.append(row[1])
     #       listC.append(row[2])
     #      listD.append(row[3])
     #      listE.append(row[4])
     #       listF.append(row[5])
     #       listG.append(row[6])
      #      listH.append(row[7])
       #     listI.append(row[8])
        #    listJ.append(row[9])
         #   listK.append(row[10])
          #  listL.append(row[11])
           # listM.append(row[12])
            
            #リスト行カウント
            listline = listline + 1
            
        print("listA=", listA)
        print("listB=", listB)
        #print("listC=", listC)
        #print("listD=", listD)
        #print("listE=", listE)
        #print("listF=", listF)
        #print("listG=", listG)
        #print("listH=", listH)
        #print("listI=", listI)
        #print("listJ=", listJ)
        #print("listK=", listK)
        #print("listL=", listL)
        #print("listM=", listM)
        #print("listline=", listline)
        
        #戻り値指定
        return listA, listB, listline #listC, listD, listE, listF, listG, listH, listI, listJ, listK, listL, listM, 

listA, listB, listline = ReadListFile(listFilePath)

class kvHostLink:
    addr = ()
    destfins = []
    srcfins = []
    port = 8501
    

    def __init__(self, host):
        self.addr = host, self.port

    def sendrecive(self, command):
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(('', self.port))
        s.settimeout(2)

        

        s.sendto(command, self.addr)
        #print("send:%r" % (command))
        rcvdata = s.recv(BUFSIZE)
         #print(s.recv)

        
        #print ('receive: %r\t Length=%r\telapsedtime = %sms' % (rcvdata, len(rcvdata), str(elapsedtime * 1000)))
        print(rcvdata)
        return rcvdata

    def mode(self, mode):
        senddata = 'M' + mode
        rcv = self.sendrecive((senddata + '\r').encode())
        return rcv

    def unittype(self):
        rcv = self.sendrecive("?k\r".encode())
        return rcv

    def errclr(self):
        senddata = 'ER'
        rcv = self.sendrecive((senddata + '\r').encode())
        return rcv

    def er(self):
        senddata = '?E'
        rcv = self.sendrecive((senddata + '\r').encode())
        return rcv

    def settime(self):
        dt_now = datetime.datetime.now()
        senddata = 'WRT ' + str(dt_now.year)[2:]
        senddata = senddata + ' ' + str(dt_now.month)
        senddata = senddata + ' ' + str(dt_now.day)
        senddata = senddata + ' ' + str(dt_now.hour)
        senddata = senddata + ' ' + str(dt_now.minute)
        senddata = senddata + ' ' + str(dt_now.second)
        senddata = senddata + ' ' + dt_now.strftime('%w')
        rcv = self.sendrecive((senddata + '\r').encode())
        return rcv
        
    def set(self, address):
        rcv = self.sendrecive(('ST ' + address + '\r').encode())
        return rcv

    def reset(self, address):
        rcv = self.sendrecive(('RS ' + address + '\r').encode())
        return rcv

    def sts(self, address, num):
        rcv = self.sendrecive(('STS ' + address + ' ' + str(num) + '\r').encode())
        return rcv

    def rss(self, address, num):
        rcv = self.sendrecive(('RSS ' + address + ' ' + str(num) + '\r').encode())
        return rcv

    def read(self, addresssuffix):
        rcv = self.sendrecive(('RD ' + addresssuffix + '\r').encode())
        return rcv

    def reads(self, addresssuffix, num):
        rcv = self.sendrecive(('RDS ' + addresssuffix + ' ' + str(num) + '\r').encode())
        return rcv

    def write(self, addresssuffix, data):
        rcv = self.sendrecive(('WR ' + addresssuffix + ' ' + data + '\r').encode())
        return rcv

    def writs(self, addresssuffix, num, data):
        rcv = self.sendrecive(('WRS ' + addresssuffix + ' ' + str(num) + ' ' + data + '\r').encode())
        return rcv


kv = kvHostLink('192.168.0.110')
#data = kv.mode('1')
#print(data)
#data = kv.er()
#print(data)
#data = kv.errclr()
#print(data)
#data = kv.unittype()
#print(data)
#data = kv.settime()
#print(data)
#data = kv.set('MR0')
#print(data)
#data = kv.reset('MR1')
#print(data)
#data = kv.sts('MR10', 5)
#print(data)
#data = kv.rss('MR10', 4)
#print(data)
scanline = 0
starttime = time.time()
while scanline < listline:
    data = kv.read(listB[scanline])
    result = int(data)
    scanline = scanline+1
    print(result)
    
elapsedtime = time.time() - starttime
print(str(elapsedtime *1000)+"ms")
#data = kv.reads('DM0.S', 4)
#print(data)
#data = kv.write('DM0.U', '1000')
#print(data)
#data = kv.writs('DM1.S', 4, '1 2 3 4')
#print(data)