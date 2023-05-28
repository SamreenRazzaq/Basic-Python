# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 14:35:15 2022

@author: DELL
"""

annual_salary=int(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percentage of your salary to save,as a decimal: "))
total_cost=int(input("Enter the cost of your dream home: "))
portion_down_payment=0.25*total_cost
current_savings=0
r=0.04
annaul_return=(current_savings*r)/12
monthly_salary=annual_salary/12
portion_saved=portion_saved*monthly_salary
time=0
while(current_savings<=portion_down_payment):
    time+=1
    current_savings+=(current_savings*r/12)+portion_saved
print("Number of Months:%d"%time)
    








