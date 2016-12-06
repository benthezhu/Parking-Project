lines = set()
with open('datapush.csv','r') as infile, open('waka.csv','w') as outfile:
    outfile.write('timestamp, tripId, route, day, timeToReachExpressStation, timeToReachDestination \n')
    lines.add('timestamp, tripId, route, day, timeToReachExpressStation, timeToReachDestination')
    next(infile)
    for line in infile:
        if line not in lines:
            # Remove whitespace
            DATA = line.strip().split(',')
            
            DATA = [d.strip() for d in DATA]
            
            # Get time to compare against
            TIME = (DATA[0])
            
            # Other data
            VEHICLECOUNT = float(DATA[1])
            TOTALSPACES = float(DATA[2])
            GARAGECODE = DATA[3]
            STREAMTIME = (DATA[4])
            
            ratio = TOTALSPACES/(VEHICLECOUNT+1)
            print(ratio)
            
            
            