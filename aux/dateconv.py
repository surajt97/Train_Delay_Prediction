import csv
def func(str):
	r = csv.reader(open('/home/suraj/Desktop/mergedmardata.csv'))
	word = str.split('/')
	day = (int)(word[0])
	day = day + 59
	ct = 0
	for row in r:
		if ct>0:
			if day==(int)(row[0]):
				arr = [row[1], row[2], row[3], row[4]]
				return arr
		ct = ct+1

print (func("12/3/2017"))