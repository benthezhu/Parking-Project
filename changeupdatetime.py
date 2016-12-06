import re
import csv
lines = set()
with open('aarhus_timechange.csv','r') as infile, open('aarhus_.csv','w') as outfile:
 # Write out column headers
   outfile.write('updatetime, vehiclecount, totalspaces, garagecode, streamtime \n')
#   lines.add('updatetime, vehiclecount, totalspaces, garagecode, streamtime \n')
   next(infile)
   for line in infile:
        if line not in lines:
            DATA = line.strip().split(',')
            DATA = [d.strip() for d in DATA]
            
            # Get time to compare against
            TIME = (DATA[0])
            
            # Other data
            VEHICLECOUNT = DATA[1]
            TOTALSPACES = DATA[2]
            GARAGECODE = DATA[3]
            STREAMTIME = (DATA[4])
            
            
            temptime = TIME.split(':')
            tempstream = STREAMTIME.split(':')
            
            time_min = temptime[0]
            time_sec = temptime[-1]
            stream_hour = (tempstream[0])
            stream_min = (tempstream[-1])
            stream_hour += stream_min
            p=int(stream_hour)
            s= int(time_min)
            time = p+s
            
           
            

            
            
                       
            outfile.write('{}, {}, {}, {}, {}\n'.format(time,VEHICLECOUNT,TOTALSPACES,GARAGECODE,stream_hour))