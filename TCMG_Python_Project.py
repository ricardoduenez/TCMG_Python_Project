from urllib.request import urlretrieve
import sys

#Variable section

date = []
year = []
num = []
url = " https://s3.amazonaws.com/tcmg476/http_access_log "
local_copy = "local_copy.txt"
total_number_request = 0

#pulling info from file

get_url = urlretrieve(url, local_copy)
amazon_file= open("local_copy.txt", "r")
if amazon_file.mode == "r":
    continue
else:
    sys.exit("Not in read mode")

#Breaking up the file into individual request

for row in temp_for_opening:
    individual_request = row.split(" ")
    date.append(split[3])
    
total_request = len(date)

print(date)
amazon_file.read(64)
amazon_file.readline()

print("Total request made in the last year:", total_request)
