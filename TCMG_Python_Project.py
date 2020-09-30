from urllib.request import urlretrieve
import sys
import os

#Variable section
date = []
pretty_version_date = [] 
day_date = []
specific_month = {}

Files = {}
file_name = []

#Request error info
error_code = []
didnt_work = 0
redirected = 0
redirect = 0
total_number = 0

oct94Count = 0
nov94Count = 0
dec94Count = 0
janCount = 0
febCount = 0 
marCount = 0
aprCount = 0
mayCount = 0
junCount = 0
julCount = 0
augCount = 0
sepCount = 0
oct95Count = 0

#pulling info from file
url = "https://s3.amazonaws.com/tcmg476/http_access_log"
local_copy = "local_copy.txt"
get_url, headers = urlretrieve(url, local_copy)
amazon_file= open(get_url, "r")

oct94 = open("Oct94.txt", "w")
nov94 = open("Nov94.txt", "w")
dec94 = open("Dec94.txt", "w")
jan = open("Jan.txt", "w")
feb = open("Feb.txt", "w")
mar = open("Mar.txt", "w")
apr = open("Apr.txt", "w")
may = open("May.txt", "w")
jun = open("Jun.txt", "w")
jul = open("Jul.txt", "w")
aug = open("Aug.txt", "w")
sep = open("Sep.txt", "w")
oct95 = open("Oct95.txt", "w")


for row in amazon_file:
      
    individual_element = row.split(" ")       
    if(len(individual_element[3]) > 14):
        date.append(individual_element[3])#Getting the Dates  
        
    if(len(individual_element)>8):
        error_code.append(individual_element[8])#Getting errors
        file_name.append(individual_element[6])#getting file names in one place

    #how many request their are
    total_request = len(date)    

    if (individual_element[3][4:7] == "Oct" and individual_element[3][8:12] == "1994"):
        oct94.write(row)
        oct94Count += 1
    if (individual_element[3][4:7] == "Nov" and individual_element[3][8:12] == "1994"):
        nov94.write(row)  
        nov94Count += 1
    if (individual_element[3][4:7] == "Nov" and individual_element[3][8:12] == "1995"):
        Dec94.write(row)  
        Dec94Count += 1    
    if (individual_element[3][4:7] == "Jan" and individual_element[3][8:12] == "1994"):
        jan.write(row)  
        janCount += 1
    if (individual_element[3][4:7] == "Feb" and individual_element[3][8:12] == "1995"):
        feb.write(row)  
        febCount += 1
    if (individual_element[3][4:7] == "Mar" and individual_element[3][8:12] == "1995"):
        mar.write(row)
        marCount += 1
    if (individual_element[3][4:7] == "Apr" and individual_element[3][8:12] == "1995"):
        apr.write(row)  
        aprCount += 1
    if (individual_element[3][4:7] == "May" and individual_element[3][8:12] == "1995"):
        may.write(row)  
        mayCount += 1    
    if (individual_element[3][4:7] == "Jun" and individual_element[3][8:12] == "1995"):
        jun.write(row)  
        junCount += 1
    if (individual_element[3][4:7] == "Jul" and individual_element[3][8:12] == "1995"):
        jul.write(row)  
        julCount += 1    
    if (individual_element[3][4:7] == "Aug" and individual_element[3][8:12] == "1995"):
        aug.write(row)  
        augCount += 1
    if (individual_element[3][4:7] == "Sep" and individual_element[3][8:12] == "1995"):
        sep.write(row)  
        sepCount += 1       
    if (individual_element[3][4:7] == "Oct" and individual_element[3][8:12] == "1995"):
        oct95.write(row)
        oct95Count += 1        
        
for dates in date:
    pretty_version_date.append(dates[1:12])
    day_date.append(dates[1:3])
    
for day in day_date:
    if(day in specific_month):
        specific_month[day] += 1
    else:
        specific_month[day] = 1
        
for messUp in error_code:
    if (messUp[0] == "3"):
        redirected += 1
    elif (messUp[0] == "4"):
        didnt_work += 1        

redirect = (redirected / total_request) * 100
didnt_work_percent = (didnt_work / total_request) * 100

for file in file_name:
    if(file in Files):
        Files[file] += 1
    else:
        Files[file] = 1
most_request = max(Files, key = Files.get)
least_request = min(Files, key = Files.get)

print(date)
amazon_file.read(64)
amazon_file.readline()
amazon_file.close()

print("October 1994 had ",oct94Count," requests.")
print("November 1994 had ",nov94Count," requests.")
print("December 1994 had ",dec94Count," requests.")
print("January 1995 had ",janCount," requests.")
print("February 1995 had ",febCount," requests.")
print("March 1995 had ",marCount," requests.")
print("April 1995 had ",aprCount," requests.")
print("May 1995 had ",mayCount," requests.")
print("June 1995 had ",junCount," requests.")
print("July 1995 had ",julCount," requests.")
print("August 1995 had ",augCount," requests.")
print("September 1995 had ",sepCount," requests.")
print("October 1995 had ",oct95Count," requests.\n")
print("There were ",total_request," total requests.\n")
print("What percent of the request did not work?\n",didnt_work_percent,"\n")
print("What percent were redirected?\n",redirect,"\n")
print("What is the most requested file?\n",most_request,"\n")
print("What is the least requested file\n",least_request,"\n")
