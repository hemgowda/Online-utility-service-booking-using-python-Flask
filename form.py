from flask_wtf import Form 
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField 
from wtforms import validators, ValidationError 
from flask import Flask, render_template, request, flash
 
class ContactForm(Form): 
 billers= SelectField('billers', choices = [('BESCOM Bangalore', 'BESCOM Bangalore'),('Chamundeshwari Electricity Supply Corp Ltd (CESCOM)', 'Chamundeshwari Electricity Supply Corp Ltd (CESCOM)'),('Gulbarga Electricity Supply Corp Ltd', 'Gulbarga Electricity Supply Corp Ltd'),('Hubli Electricity Supply Company Ltd (HESCOM)', 'Hubli Electricity Supply Company Ltd (HESCOM)'),('Mangalore Electricity Supply Company LTD (Non RAPDR)', 'Mangalore Electricity Supply Company LTD (Non RAPDR)'),])
 customer_id = TextField("customer_id",[validators.Required("Please enter required field")])   
 payment_method =  SelectField('payment_method', choices = [('Net banking', 'Net banking'),('debit card', 'debit card'),('credit card', 'credit card'),('UPI', 'UPI'),])
 billing_type = SelectField('billing_type', choices = [('Water bill', 'Water bill'),('Electricity bill', 'Electricity bill'),('Mobile recharge', 'Mobile recharge'),('DTH', 'DTH'),])
 billing_cost = TextField("billing_cost",[validators.Required("Please enter required field")])
 submit = SubmitField("Submit") 