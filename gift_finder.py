#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 12:06:50 2018

@author: finc123
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"