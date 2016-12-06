with open('waka.csv','r') as infile, open('dataformodel.csv','w') as outfile:
    for line in infile:
        DATA = [d.strip() for d in  line.strip().split(',')]
        outfile.write('{},{},{},{},{},{}\n'.format(DATA[0],DATA[1],DATA[2],DATA[3],DATA[4],DATA[5]))