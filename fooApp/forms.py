# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 21:20:05 2020

@author: anali
"""

#WTForms provides HTML form generation and validation of form data => find submitted form data on the post and put requests
from wtforms import Form 
from wtforms import TextAreaField, TextField, FloatField
from wtforms.validators import Length, NumberRange,required

class ProductForm(Form):
  name = TextField('Name', [Length(max=255)])
  description = TextAreaField('Description')
  price = FloatField('price',[NumberRange(0.00),required()] )

from wtforms import PasswordField

class LoginForm(Form):
    """Render HTML input for user login form.

    Authentication (i.e. password verification) happens in the view function.
    """
    username = TextField('Username', [required()])
    password = PasswordField('Password', [required()])
    
