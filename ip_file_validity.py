# -*- coding: utf-8 -*-
"""
Created on Sun May 23 09:43:08 2021

@author: vedant
"""

import os 
import sys

def ip_file_valid():
    
    #Prompt user to enter the path to the file
    ip_file=input("Enter the path to the ip file: \n")
    
    ##Checking if file exists
    if (os.path.isfile(ip_file))==True:
        print("\n IP File is valid\n")
    else:
        print("\n IP file {} does not exist\n Please check and try again.\n".format(ip_file))
        sys.exit()
    
    ##Reading the file
    selected_ip_file=open(ip_file,'r')
    
    ##starting from beginning of file
    selected_ip_file.seek(0)
    
    #Reading each line from the file
    ip_list=selected_ip_file.readlines()
    
    ##Close the file
    selected_ip_file.close()
    
    print(ip_list)
    return ip_list
    

#ip_file_valid()