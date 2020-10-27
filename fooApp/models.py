# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 21:20:43 2020

@author: anali
"""
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'foodb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/foodb'

mongo = PyMongo(app)