import csv
r = csv.reader(open('/home/suraj/Desktop/mmar.csv'))
writer = csv.writer(open('/home/suraj/Desktop/mmarf.csv', 'w'))
ct = 0
for row in r:
	if ct>0:
		s = row[0]
		word = s.split()
		day = (int)(word[2])
		day = day + 59
		#print day
		tempLow = word[4]
		tempHi = word[3]
		row[0] = day
		row[1] = tempLow
		row[2] = tempHi
		writer.writerow(row)
	ct = ct+1
