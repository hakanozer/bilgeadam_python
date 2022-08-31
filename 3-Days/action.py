#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:40:05 2022

@author: hakan
"""
import re

def sum( num1, num2 ):
    return num1 + num2

def minus( num1, num2 ):
    return num1 - num2

cities = ["İstanbul", "İzmir", "Ankara", "Adana"]

cityArr = [
    {"no": "34", "name": "İstanbul"  },
    {"no": "35", "name": "İzmir"  },
    {"no": "06", "name": "Ankara"  },
    {"no": "01", "name": "Adana"  },
]

months = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"];

def emailValid(email):
    pattern = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    regex = re.compile(pattern)
    if re.fullmatch(regex, email):
        return True
    else:
        return False