'''
For OIT248
Tim Nichols, Varshith Dondapati, Stephanie Scott, Stella Chen


'''


import csv
from gurobipy import *


#define model configuration

















# import route data

file = open("files/routes.csv", "rU")
csvFile = csv.reader(file)

# Pull out headers
Header = csvFile.next()

# Make a multidict with all patient information
route_name, route_distance, route_hours, service_hours, loops_day, active_evs = multidict({row[0]: row[1:len(Header)] for row in csvFile})

# Fix data type for Age, Waiting Time, and Life Expectancy, since they are all currently stored as strings (characters)
for r in route_name:
	
	route_distance[r] = float(route_distance[r])
	route_hours[r] = float(route_hours[r])
	service_hours[r] = float(service_hours[r])
	loops_day[r] = int(loops_day[r])
	active_evs[r] = int(active_evs[r])


# import price data 

print route_distance





