#Import OS module
#This will allow to create file paths acroos operating systems
import os
#Import Counter module to get candidate votes 
from collections import Counter
#Import CSV file module
import csv  
#Specify file path
csvpath=os.path.join('Resources','election_data.csv')
#Open file in read mode  
with open(csvpath) as csvfile: 
  #Pass the file object to reader() to get the reader object
  csvreader=csv.reader(csvfile,delimiter=',')
  #This stores a reference to file stream
  print(csvreader)
  #Read the header row first
  csv_header=next(csvreader)
  print(f"CSV Header:{csv_header}")
  #Iterate over each row in the CSV using reader object
  for row in csvreader:
    #Row variable is a list that represents a row in CSV
    print(row)     
  csvfile.seek(0,os.SEEK_SET)      
  lines=[line for line in csvreader]
  counts=Counter(l[2] for l in lines)  
  total_votes=counts['Khan']+counts['Correy']+counts['Li']+counts["O'Tooley"]
  fraction_khan=counts['Khan']/total_votes
  percent_khan="{:.3%}".format(fraction_khan)
  fraction_correy=counts['Correy']/total_votes
  percent_correy="{:.3%}".format(fraction_correy)
  fraction_li=counts['Li']/total_votes
  percent_li="{:.3%}".format(fraction_li)
  fraction_otooley=counts["O'Tooley"]/total_votes 
  percent_otooley="{:.3%}".format(fraction_otooley)
  otooley=counts["O'Tooley"]
  print()
  print(" Election Results")
  print(" ------------------")
  print(f" Total Votes : {total_votes}")
  print(" ------------------")
  print(f" Khan : {percent_khan} ({counts['Khan']})")
  print(f" Correy : {percent_correy} ({counts['Correy']})")
  print(f" Li : {percent_li} ({counts['Li']})")
  print(f" O'Tooley : {percent_otooley} ({otooley})")
  print(" ------------------")
  print(f" Winner : Khan")
  output=f'''

            Election Results
            -----------------------------
            Total Votes : {total_votes}
            -----------------------------
            Khan : {percent_khan} ({counts['Khan']})
            Correy : {percent_correy} ({counts['Correy']})
            Li : {percent_li} ({counts['Li']})
            O'Tooley : {percent_otooley} ({otooley})
            -----------------------------
            Winner : Khan
         '''    
  with open("analysis.txt","w") as file_handler:
    file_handler.write(output)
    file_handler.close()