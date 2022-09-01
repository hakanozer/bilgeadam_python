#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:41:24 2022

@author: hakan
"""

import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bilgeadam_python'
    )