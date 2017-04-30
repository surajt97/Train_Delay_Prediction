
import csv 
a = csv.reader(open('/home/suraj/Desktop/d/fd1.csv'))
b = csv.reader(open('/home/suraj/Desktop/d/fd2.csv'))
c = csv.reader(open('/home/suraj/Desktop/d/fd3.csv'))
d = csv.reader(open('/home/suraj/Desktop/d/fd4.csv'))
e = csv.reader(open('/home/suraj/Desktop/d/fd5.csv'))
f = csv.reader(open('/home/suraj/Desktop/d/fd6.csv'))
g = csv.reader(open('/home/suraj/Desktop/d/fd7.csv'))
h = csv.reader(open('/home/suraj/Desktop/d/fd8.csv'))
i = csv.reader(open('/home/suraj/Desktop/d/fd9.csv'))
j = csv.reader(open('/home/suraj/Desktop/d/fd10.csv'))
k = csv.reader(open('/home/suraj/Desktop/d/fd11.csv'))
l = csv.reader(open('/home/suraj/Desktop/d/fd12.csv'))
writer = csv.writer(open('/home/suraj/Desktop/d/finalD.csv', 'w'))
for row in a:
    writer.writerow(row)
ct = 0
for row in b:
    if ct>0:
        writer.writerow(row)
    ct = ct+1
ct = 0
for row in c:
    if ct>0:
        writer.writerow(row)
    ct = ct+1
ct = 0
for row in d:
    if ct>0:
        writer.writerow(row)
    ct = ct+1
ct = 0
for row in e:
    if ct>0:
        writer.writerow(row)
    ct = ct+1
ct = 0
for row in f:
    if ct>0:
        writer.writerow(row)
    ct = ct+1
ct = 0
for row in g:
    if ct>0:
        writer.writerow(row)
    ct = ct+1
ct = 0
for row in h:
    if ct>0:
        writer.writerow(row)
    ct = ct+1
ct = 0
for row in i:
    if ct>0:
        writer.writerow(row)
    ct = ct+1
ct = 0
for row in j:
    if ct>0:
        writer.writerow(row)
    ct = ct+1
ct = 0
for row in k:
    if ct>0:
        writer.writerow(row)
    ct = ct+1
ct = 0
for row in l    :
    if ct>0:
        writer.writerow(row)
    ct = ct+1



