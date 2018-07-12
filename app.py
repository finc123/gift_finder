#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 12:06:50 2018

@author: finc123
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html') #by default flask looks in the 'templates' folder, so create folder called templates