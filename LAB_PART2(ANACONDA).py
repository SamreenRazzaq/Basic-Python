#Part B: Saving with a raise

annual_salary= float(input("Enter your annual salary: "))
portion_saved= float(input("Enter the percent of your salary to save, as a decimal: "))
# cost of dream house
total_cost= float (input("Enter the cost of your dream home: "))
#enter raise after 6 months
semi_annual_raise=float (input("Enter the semi-­annual raise, as a decimal:"))



portion_down_payment= 0.25*total_cost
current_savings= 0
r=0.04
months=0
while current_savings<=portion_down_payment:
    months+=1
    current_savings+= (current_savings*r/12)+(annual_salary*portion_saved/12)
    if months%6==0:
        annual_salary+=annual_salary*semi_annual_raise
       
    
print ("Number of months: ",months)

