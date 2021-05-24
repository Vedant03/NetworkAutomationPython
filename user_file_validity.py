# -*- coding: utf-8 -*-
"""
Created on Sun May 23 09:44:57 2021

@author: vedant
"""

import paramiko
import os
import sys
import re
import time


###checking usernmae/password file
user_file=input("\nEnter the filepath and name: \n")

##verifying the path and file
if os.path.isfile(user_file)==True:
    print("File is valid")
else:
    print("Invalid file")
        #sys.exit()
    
#user_file_valid()


cmd_file=input("\nEnter the filepath and name containing commands: \n")
    
##verifying the path and file
if os.path.isfile(cmd_file)==True:
    print("File is valid")
else:
    print("Invalid file")
    #sys.exit()
        
def ssh_connect(ip):
    global user_file
    global cmd_file
    
    ##creating SSH connection
    try:
        selected_user_file=open(user_file,'r')
        
        selected_user_file.seek(0)
        username=selected_user_file.readlines()[0].split(",")[0].rstrip("/n")
        
        selected_user_file.seek(0)
        password=selected_user_file.readlines()[0].split(",")[1].rstrip("/n")
        
        ##logging into the device
        session=paramiko.SSHClient()
        
        ##Setting auto accepting unknown key hosts
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        ##make ssh session to ip with username and password and port
        session.connect(ip.rstrip("/n"),username=username,password=password,port=22)
   
        ##start interactive shell session
        connection=session.invoke_shell()
        
        ##setting terminal length
        connection.send("enable\n")
        connection.send("terminal length\n")
        time.sleep(1)
        
        ##open cmd_file to send commands and set cursor at start
        selected_cmd_file=open(cmd_file,'r')
        selected_cmd_file.seek(0)
        
        ##Writing config on the device
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line+'/n')
            time.sleep(1)
            
        selected_user_file.close()
        selected_cmd_file.close()
        
        session.close()
        
    except paramiko.AuthenticationException:
        print("Invalid username or password")
            
#ssh_connect('127.0.0.1')    
    