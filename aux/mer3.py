
import csv 
r = csv.reader(open('/home/suraj/Desktop/d/d_10.csv'))
writer = csv.writer(open('/home/suraj/Desktop/d/fm10.csv', 'w'))
ct = 0
for row in r:
    if ct==0:
        x = ['date', 'weather', 'tempHigh', 'tempLow']
        writer.writerow(x)
    if ct>0:
        if ct%4==2:
            s = row[5]
            w = s.split()
            bday = (int)(w[1])
            bmonth = (int)(w[2])
            if bmonth==2:
                 bday = (int)((int)(bday) + 31)
            elif bmonth==3:
                 bday =  (int)((int)(bday) + 59)       
            elif bmonth==4:
                 bday =  (int)((int)(bday) + 90)       
            elif bmonth==5:
                 bday =  (int)((int)(bday) + 120)      
            elif bmonth==6:
                 bday =  (int)((int)(bday) + 151)  
            elif bmonth==7:
                 bday =  (int)((int)(bday) + 181)  
            elif bmonth==8:
                 bday =  (int)((int)(bday) + 212)  
            elif bmonth==9:
                 bday =  (int)((int)(bday) + 243)  
            elif bmonth==10:
                 bday =  (int)((int)(bday) + 273)  
            elif bmonth==11:
                 bday =  (int)((int)(bday) + 304)  
            elif bmonth==12:
                 bday =  (int)((int)(bday) + 334) 
            row[0] = bday
            x = [row[0], row[7], row[8], row[9]]
            writer.writerow(x)
    ct = ct+1



