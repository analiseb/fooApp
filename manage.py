# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:57:23 2020

@author: anali
"""
from flask_script import Manager
from fooApp.app import app

manager = Manager(app)
app.config['DEBUG'] = True # Ensure debugger will load.

if __name__ == '__main__':
  manager.run()