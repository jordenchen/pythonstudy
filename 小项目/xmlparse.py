#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-04-25 14:29:25
# @Last Modified by:   anchen
# @Last Modified time: 2018-05-02 14:13:51

import  xml.etree.ElementTree as ET

tree = ET.parse('sitemap-11.xml')
root = tree.getroot()

f = open('rs.txt','w')

for loc in root.iter('loc'):
    if loc.text.find('history_price',0)!=-1:
        f.write(loc.text+'\n')
f.close()


