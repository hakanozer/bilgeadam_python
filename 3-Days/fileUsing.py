#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:51:13 2022

@author: hakan
"""


def crateFile():
    try:
        f = open('sample.txt', 'x')
    except Exception:
        pass


def fileWrite(data):
    status = False
    ls = fileRead()
    for line in ls:
        if line.replace("\n", "") == data:
            status = True
            
    if status == False:
        f = open("sample.txt", "a")
        f.write("{}\n".format(data))
        f.close()
    
    
def fileRead():
    lines = []
    f = open("sample.txt", "r")
    for line in f:
        lines.append(line)
    f.close()    
    return lines