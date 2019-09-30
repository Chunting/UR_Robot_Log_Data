#!/usr/bin/python
# -*- coding: UTF-8 -*-
import record1
#import test_sensor 
import threading
import time
 
exitFlag = 0
 
class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, host, port, csvfilename):
        threading.Thread.__init__(self)
        self.HOST = host
        self.POST = port
        self.CSVFINENAME = csvfilename
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        print "Starting " + self.CSVFINENAME
        record_left(self.HOST,self.PORT, self.CSVFINENAME)
        print "Exiting " + self.CSVFINENAME


def main():
    HOST_LEFT = '192.168.1.101'
    HOST_RIGHT = '192.168.1.102'
    PORT = 30004
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
    CSVFINENAME_LEFT="~/Documents/rtde1/examples/data/"+now+r"_ur_left.csv"
    CSVFINENAME_RIGHT="~/Documents/rtde1/examples/data/"+now+r"_ur_right.csv"
    # 创建新线程
    thread1 = myThread(HOST_LEFT, PORT,CSVFINENAME_LEFT)
    thread2 = myThread(HOST_RIGHT, PORT,CSVFINENAME_RIGHT)
 
    # 开启线程
    thread1.start()
    thread2.start()
 
    print "Exiting Main Thread"
    
    

if __name__ == '__main__':
    main()
    # print(__name__)
 

