'''
For OIT248
Tim Nichols, Varshith Dondapati, Stephanie Scott, Stella Chen

'''

import csv
from gurobipy import *

#define model configuration
#######################################################################################################
# Section 1 - Data  

###------------------------------charging station data (Tim or Varsh to fill out)---------------------
#this could be an extension if we have time, ignore for now, assuming one type of charging station, and 
#assuming the number of charging station is larger than the number of buses
#cannot charge battery faster than the charging station speed
max_charing_speed = 0

###----------------------------------battery characteristics data------------------------------------
#data for battery capacity and duration, need to be updated, battery capacity in kw, duration in hour
#this part need to be updated if we are considering multiple bus types with different battery configurations
max_battery_capacity = 0
battery_duration = 0
#roundtrip efficiency for battery
battery_efficiency = 0

###---------------------------------- import route data----------------------------------------------

file = open("files/routes.csv", "rU")
csvFile = csv.reader(file)

# Pull out headers
Header = csvFile.next()

# Make a multidict with all route information
route_name, route_distance, route_hours, service_hours, loops_day, active_evs = multidict({row[0]: row[1:len(Header)] for row in csvFile})

# Fix data type for route distance, route hours, service hours, loops per day, and active evs, since they are all currently stored as strings (characters)
for r in route_name:
	
	route_distance[r] = float(route_distance[r])
	route_hours[r] = float(route_hours[r])
	service_hours[r] = float(service_hours[r])
	loops_day[r] = int(loops_day[r])
	active_evs[r] = int(active_evs[r])
	
###--------------------------- end of import route data -----------------------------------------------

###------------------------- import electricity price data --------------------------------------------

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

#print summer_weekend
###--------------------------end of import electricity price data -----------------------
#########################################################################################
# Section 2 - Create Model 
MGModel = Model("Stanford Marguerite Schedule")	

#########################################################################################
# Section 3 - Create your Decision Variables

Assign = {}

Time = list(range(0,24))
Vehicles = ["B1", "B2", "B3", "B4", "B5", "B6", "B7"]

# for n in Vehicles:
# 	for t in Time:
# 		for r in Routes:
# 			Assign[(t, c, g)] = MGModel.addVar(vtype = GRB.BINARY, name = "Assign_" + t + "_" + c + "_" + r) 

# TANK = {}
# 
# TANK = AirGateModel.addVar(lb = 0, ub = GRB.INFINITY, name = "TANK")
# 

### route_assignment: for each bus, for each hour, choose route assignment (0,1,2,3,4,5)

### charge_or_not: for each bus, for each hour, binary decision variable to determine charging (1), or not charging (0)

### charge_rate: for each bus, for each hour, continuous decision variable of rate of charging, bounded by highest charge rate
 


#########################################################################################
#Section 4 - Update model to include decision variables
MGModel.update()	


#########################################################################################
#Section 5 - Build Objective and Set the Objective


#########################################################################################
#Section 6 - Add Constraints
## constraint 1: # of buses allowed on the same route at the same time
## constraint 2: # of hours it takes to complete each route

## State-of-charge constraint, cannot over charge the batteries to exceed the maximum capacity of the battery

## Cannot be charging if the bus in on a route  
    ##if route_assignment is not 0, charge_or_not = 0 
    ##if route_assignment is 0, charge_or_not can be 0 or 1
    ##if charge_or_not = 0, charge_rate = 0
    ##if charge_or_not = 1, 0<charge_rate<max_charge_rate


#########################################################################################
# Section 7 - Solve the model! 
# MGModel.optimize()	




