# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:21:09 2021

@author: vedant
"""
import threading

def create_threads(list3,function):
    threads=[]
    
    for ip in list3:
        th=threading.Thread(target=function,args=(ip,))
        th.start()
        threads.append(th)
        
    for th in threads:
        th.join()
        
