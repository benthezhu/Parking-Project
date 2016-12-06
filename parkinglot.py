lines = set()
with open('data.csv','r') as infile, open('data_S.csv','w') as outfile:
    outfile.write('timestamp, tripId, route, day, timeToReachExpressStation, timeToReachDestination \n')
    lines.add('timestamp, tripId, route, day, timeToReachExpressStation, timeToReachDestination')
    for line in infile:
        if line not in lines:
            # Remove whitespace
            l = line.strip().split(',')
            l = [_l.strip() for _l in l]
            # Check line
            ID = l[1]
            LINE = ID.split('..')
            try:
                LINE = LINE[1]
                DIR = LINE[0]
                if DIR == 'S':
                    outfile.write(line)
                    lines.add(line)
            except:
                continue
