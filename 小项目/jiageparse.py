#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-05-02 14:14:51
# @Last Modified by:   anchen
# @Last Modified time: 2018-05-02 16:17:50

from urllib import request
import re

file1 = open('rs.txt','r')
file2 = open('jiage.txt','w')

for line in file1:
    for i in range(1,7):
        line = line[:-6] + '-0' +str(i)+'.html'
        print(line)
        response = request.urlopen(line)
        matchObj = re.search(r'font-bold red',response)
        if  matchObj:
            file2.write(line)

file1.close()
file2.clolse()