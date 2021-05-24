# -*- coding: utf-8 -*-
"""
Created on Sun May 23 09:44:53 2021

@author: vedant
"""
import sys
#l1=['172.17.2.191/n', '172.17.2.256/n']
def ip_valid(list1):
    
    ##Reading the iplist and removing /n from the ip and making a list of octect
    for ip in list1:
        print(ip)
        
        ##Strip the /n
        ip=ip.rstrip("/n")
        print(ip)
        
        ##Create list of the ip address
        octetlist=ip.split(".")
        print(type(octetlist))
        
        ##Check ip validity
        if(len((octetlist))==4 and (1<=int(octetlist[0])<=223) and int(octetlist[0])!=127 and int(octetlist[0])!=169
           and 1<=int(octetlist[1])<=255 and  1<=int(octetlist[2])<=255 and  1<=int(octetlist[3])<=255):
           print("{} is valid".format(ip))
           continue
       
        else:
           print("{} is invalid".format(ip)) 
           sys.exit()
           
#ip_valid(l1)
        
        
    
        