#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import signal
import os
from time import sleep

is_exit=0
def f(a,b):
    global is_exit
    is_exit=1
    print 'kill me'
    os.kill(os.getpid(),signal.SIGKILL)

def tf():
    while not is_exit:
        sleep(20)

signal.signal(signal.SIGINT,f)
p=threading.Thread(target=tf)
p.start()
while 1:
    sleep(10)

print 'done'