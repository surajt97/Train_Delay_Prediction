import csv 
def conv(day, month):
    if month==2:
        day = day + 31
    elif month==3:
        day = day + 59
    elif month==4:
        day = day + 90
    elif month==5:
        day = day + 120
    elif month==6:
        day = day + 151
    elif month==7:
        day = day + 181
    elif month==8:
        day = day + 212
    elif month==9:
        day = day + 243
    elif month==10:
        day = day + 273
    elif month==11:
        day = day + 304
    elif month==12:
        day = day + 334

    return day