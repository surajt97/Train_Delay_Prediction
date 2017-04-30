import csv
r = csv.reader(open('/home/suraj/Desktop/data.csv'))
writer = csv.writer(open('/home/suraj/Desktop/o.csv', 'w'))
ct = 0
for row in r:
	if ct>0 :
		s = row[5]
		words = s.split()
		row[0] = words[1]
		row[2] = words[3]
		if words[2]=='January':
			row[1] = 1
		elif words[2]=='February':
			row[1] = 2	
		elif words[2]=='March':
			row[1] = 3	
		elif words[2]=='April':
			row[1] = 4	
		elif words[2]=='May':
			row[1] = 5	
		elif words[2]=='June':
			row[1] = 6	
		elif words[2]=='July':
			row[1] = 7	
		elif words[2]=='August':
			row[1] = 8	
		elif words[2]=='September':
			row[1] = 9	
		elif words[2]=='October':
			row[1] = 10	
		elif words[2]=='November':
			row[1] = 11	
		elif words[2]=='December':
			row[1] = 12	
	ct = ct+1
	writer.writerow(row)

