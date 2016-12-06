lines = set()
with open('aarhus_parking.csv','r') as infile, open('data_final_2.csv','w') as outfile:
    
    # Write out column headers
    outfile.write('updatetime, vehiclecount, totalspaces, garagecode, streamtime \n')
    lines.add('updatetime, vehiclecount, totalspaces, garagecode, streamtime \n')
    
    for line in infile:
        if line not in lines:
            
            # Get data for each line
            DATA = line.strip().split(',')
            DATA = [d.strip() for d in DATA]
            
            # Get time to compare against
            TIME = DATA[0]
            
            # Other data
            VEHICLECOUNT = DATA[1]
            TOTALSPACES = DATA[2]
            GARAGEID = DATA[3]
            STREAMTIME = DATA[4]
            
            tempstream = [int(x) for x in STREAMTIME.split(':')]
            tempupdate = [int(x) for x in TIME.split(':')]
            time_stream = 0
            time_update = 0
            for tempstream, tempupdate, time_stream, time_update, in zip(temp_96, [60, 1], temp_42, [60, 1]):
                time_96 += t_96*t1
                time_42 += t_42*t2
                
            TIMETOREACHEXPRESSSTATION = str(time_96)
            TIMETOREACHDESTINAION = str(time_42)
            
            outfile.write('{}, {}, {}, {}, {}, {}, {}\n'.format(TIME, TRIPID, ROUTE, DAY, TIMETOREACHEXPRESSSTATION, TIMETOREACHDESTINAION, SWITCH))