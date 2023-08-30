# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:51:36 2023

@author: FutureCode
"""
import re
#"[A-Za-z]+ [A-Za-z]' '[0-9]' '[0-9]:[0-9]:[0-9]' '[0-9]"
text = 'Tue '
reg = "[A-Za-z]+ "
if re.match(reg,text):
    print('Правельно')
else:
    print('Неправильно')
text = 'Aug '    
reg = "[A-Za-z]+ "    
if re.match(reg,text):
    print('Правельно')
else:
    print('Неправильно')
    
text = '29 '    
reg = "[0-9]+ "
if re.match(reg,text):
    print('Правельно')
else:
    print('Неправильно')
    
    
text = '17:51:36 '    
reg = "[0-9]+\:[0-9]+\:[0-9]+ "
if re.match(reg,text):
    print('Правельно')
else:
    print('Неправильно')

text = '2023'
reg = "[0-9]+"
if re.match(reg,text):
    print('Правельно')
else:
    print('Неправильно')
    
    