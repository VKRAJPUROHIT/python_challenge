#Import OS module
#This will allow to create file paths acroos operating systems
import os
#Import CSV file module
import csv  
#Import Datetime module
import datetime  
#Specify file path   
csvpath=os.path.join('Resources','budget_data.csv')
#Open file in read mode 
with open(csvpath) as csvfile:
  #Pass the file object to reader() to get the reader object
  csvreader=csv.reader(csvfile,delimiter=',')
  print(csvreader)
  #Read the header row first
  csv_header=next(csvreader)
  print(f"CSV Header:{csv_header}")
  #Read the first row with data 
  row=next(csvreader)
  print(row)
  #Initialize total_months counter,net_total_amount counter,start_profit counter,sum_of_profit_change counter at the first row 
  greatest_increase=0
  greatest_decrease=0
  total_months=1
  net_total_amount=int(row[1])
  start_profit=int(row[1])
  sum_of_profit_change=0
  #Iterate over each row in the csv using reader object 
  for row in csvreader:     
    #Increment the total_months counter by 1
    total_months=total_months+1
    #Increment the net_total_amount by Profit/Losses and calculate profit changes    
    net_total_amount=net_total_amount+int(row[1])       
    profit_change=int(row[1])-start_profit         
    start_profit= int(row[1])
    sum_of_profit_change=sum_of_profit_change+profit_change       
    if profit_change>greatest_increase:
      greatest_increase=profit_change
      increase_date=row[0] 
    elif profit_change<greatest_decrease:
      greatest_decrease=profit_change
      decrease_date=row[0]
    else:
      pass  
    #Row variable is a list that represents a row in csv
    print(row) 
  else:
    #Calculate average change to two decimal places 
    average_of_profit_change=round(sum_of_profit_change/(total_months-1),2)
    output=f'''
              
              Financial Analysis

              ---------------------

              Total Months : {total_months}
              Total : ${net_total_amount}
              Average change : ${average_of_profit_change}
              Greatest Increase in Profits : {increase_date} (${greatest_increase})
              Greatest Decrease in Profits : {decrease_date} (${greatest_decrease})
            '''
    print()
    print(" Financial Analysis")
    print() 
    print(" -------------------------")
    print()
    print(f" Total Months : {total_months}")    
    print(f" Total : ${net_total_amount}")
    print(f" Average change : ${average_of_profit_change}")
    print(f" Greatest Increase in Profits : {increase_date} (${greatest_increase})")
    print(f" Greatest Decrease in Profits : {decrease_date} (${greatest_decrease})")
    with open("analysis.txt","w") as file_handler:
      file_handler.write (output) 
      file_handler.close()