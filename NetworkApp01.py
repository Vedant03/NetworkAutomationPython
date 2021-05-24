# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:24:47 2021

@author: vedant
"""

##importing necessary modules

import sys
from ip_file_validity import ip_file_valid
from ip_validity import ip_valid
from ip_connectivity import ip_reach
#from user_file_validity import user_file_valid
#from user_file_validity import user_commands
from user_file_validity import ssh_connect
from create_threads import create_threads

##saving list of ip address
ip_list=ip_file_valid

try:
    ip_valid(ip_list)
except KeyboardInterrupt:
    print("\nProgram aborted by user\n")
    sys.exit()
    
try:
    ip_reach(ip_list)
except KeyboardInterrupt:
    print("\nProgram aborted\n")
    sys.exit()
    
create_threads(ip_list,ssh_connect)