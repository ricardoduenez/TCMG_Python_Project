from urllib.request import urlretrieve
import sys

#Variable section
date = []
url = "https://s3.amazonaws.com/tcmg476/http_access_log"
local_copy = "local_copy.txt"
total_number_request = 0

#pulling info from file
get_url, headers = urlretrieve(url, local_copy)
amazon_file= open(get_url, "r")



#Breaking up the file into individual request
for row in amazon_file:
    
    #Checking to see if the file is in the right mode
    #if amazon_file.mode == "r":
    #    continue
    #else:
    #    sys.exit("Not in read mode")
        
    individual_request = row.split(" ")
    date.append(individual_request[3])
    
total_request = len(date)

print(date)
amazon_file.read(64)
amazon_file.readline()
amazon_file.close()

print("Total request made in the last year:", total_request)
