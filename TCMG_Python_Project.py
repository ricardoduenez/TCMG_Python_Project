from urllib.request import urlretrieve
import sys
import os

#Variable section
date = []
pretty_version_date = [] 
day_date = []
specific_month = {}

#Last 365 days
last_year = []

Files = {}
file_name = []

#Request error info
error_code = []
didnt_work = 0
redirected = 0
redirect = 0
url = "https://s3.amazonaws.com/tcmg476/http_access_log"
local_copy = "local_copy.txt"
total_number = 0

oct94count = 0
nov94count = 0
dec94count = 0
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
get_url, headers = urlretrieve(url, local_copy)
amazon_file= open(get_url, "r")



#Breaking up the file into individual request
for row in amazon_file:
    
    #Getting the Dates    
    individual_request = row.split(" ")
    date.append(individual_request[3])
    
    #how many request their are
    total_request = len(date)
    
    #
    if(len(individual_request) > 8):
        error_code.append(individual_request[8])
        file_name.append(individual_request[8])
    elif (len(individual_request[3]) > 14):
        date.append(individual_request[3])

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


print("What percent of the request did not work?\n",didnt_work_percent,"\n")
print("What percent were redirected?\n",redirect,"\n")
print("What is the most requested file?\n",most_request,"\n")
print("What is the least requested file\n",least_request,"\n")
