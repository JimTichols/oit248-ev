'''
For OIT248
Tim Nichols, Varshith Dondapati, Stephanie Scott, Stella Chen


'''


import csv
from gurobipy import *


#define model configuration



+#data for charging station, Tim or Varsh to fill out
 +max_charge_rate = 0 
 +min_charge_rate = 0
  













# import route data

file = open("files/routes.csv", "rU")
csvFile = csv.reader(file)

# Pull out headers
Header = csvFile.next()

# Make a multidict with all route information
route_name, route_distance, route_hours, service_hours, loops_day, active_evs = multidict({row[0]: row[1:len(Header)] for row in csvFile})

# Fix data type for Age, Waiting Time, and Life Expectancy, since they are all currently stored as strings (characters)
for r in route_name:
	
	route_distance[r] = float(route_distance[r])
	route_hours[r] = float(route_hours[r])
	service_hours[r] = float(service_hours[r])
	loops_day[r] = int(loops_day[r])
	active_evs[r] = int(active_evs[r])


# import price data 

file = open("files/prices.csv", "rU")
csvFile = csv.reader(file)

# Pull out headers
Header = csvFile.next()

# Make a multidict with all patient information
hour_price,	summer_weekday,	summer_weekend,	winter_weekday,	winter_weekend = multidict({row[0]: row[1:len(Header)] for row in csvFile})

# Fix data type for Age, Waiting Time, and Life Expectancy, since they are all currently stored as strings (characters)
for h in hour_price:
	summer_weekday[h] = float(summer_weekday[h])
	summer_weekend[h] = float(summer_weekend[h])
	winter_weekday[h] = float(winter_weekday[h])
	winter_weekend[h] = float(winter_weekend[h])

print summer_weekend


# build objective function
 +
 +
 +
 +
 +# build decision variables
 +### route_assignment: for each bus, for each hour, choose route assignment (0,1,2,3,4,5)
 +
 +### charge_or_not: for each bus, for each hour, binary decision variable to determine charging (1), or not charging (0)
 +
 +### charge_rate: for each bus, for each hour, continuous decision variable of rate of charging, bounded by highest charge rate
 +
 +
 +
 +# build constraints
 +## constraint 1: # of buses allowed on the same route at the same time
 +
 +## constraint 2: # of hours it takes to complete each route
 +
 +## State-of-charge constraint, cannot over charge the batteries to exceed the maximum capacity of the battery
 +
 +## Cannot be charging if the bus in on a route
 +   ##if route_assignment is not 0, charge_or_not = 0 
 +   ##if route_assignment is 0, charge_or_not can be 0 or 1
 +   ##if charge_or_not = 0, charge_rate = 0
 +   ##if charge_or_not = 1, 0<charge_rate<max_charge_rate
 +


