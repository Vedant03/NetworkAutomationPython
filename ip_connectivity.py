# -*- coding: utf-8 -*-
"""
Created on Sun May 23 09:44:55 2021

@author: vedant
"""
import subprocess


#l1=['127.0.0.1/n', '172.17.2.256/n']
def ip_reach(list2):
    
    for ip in list2:
        
        ip=ip.rstrip("/n")
        print((ip))
        
        ping_response=subprocess.call('ping %s /n 2' % (ip),stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        
        if(ping_response==0):
            print("{} is reachable".format(ip))
            continue
        
        else:
            print("{} is unreachable".format(ip))
           

        
#ip_reach(l1)