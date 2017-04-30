#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
import SocketServer
#import cgi
#import csv as csv
#import numpy as np
#import pandas as pd

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        string12 = query_components['string1']
        string23 = query_components['string2']
        #string12 is the train number
        #string23 is the date entered by the user
        print(string12)
        print(string23)

        delay = final_function(string23,string12)
        delay1 = (int)(delay)
        delaystr = (str)(delay1)
        
        #delay. 
        self._set_headers()
        self.wfile.write(delaystr)

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        self._set_headers()


    #######################TRAIN DELAY CALCULATION############################
    global final_function
    def final_function(str1,str2):
      def conv(str1):
            words = word = str1.split('/')
            day = int(word[0])
            month = int(word[1])
            if month == 2:
                day = day + 31
            elif month == 3:
                day = day + 59
            elif month == 4:
                day = day + 90
            elif month == 5:
                day = day + 120
            elif month == 6:
                day = day + 151
            elif month == 7:
                day = day + 181
            elif month == 8:
                day = day + 212
            elif month == 9:
                day = day + 243
            elif month == 10:
                day = day + 273
            elif month == 11:
                day = day + 304
            elif month == 12:
                day = day + 334

            return day


      def func(str1):
            r = csv.reader(open('mergedmardata.csv'))
            word = str1.split('/')
            day = (int)(word[0])
            day = day + 59
            ct = 0
            for row in r:
                if ct > 0:
                    if day == int(row[0]):
                        arr = [row[1], row[2], row[3], row[4]]
                        arr = np.asarray(arr)
                        return arr
                ct = ct + 1
      #print(func(str1))
      #print(conv(str1))
      df = pd.read_csv('final_data.csv')

      df.iloc[np.random.permutation(len(df))]
      Features = df[list(df.columns)[:-1]]
      delay = df['delay']

      sday = conv(str1)
      eday = sday +1
      stime =  1060
      temp = func(str1)

      #test1 = np.concatenate(sday,stime)
      d = {'sday': sday,'stime': 1060, 'eday': eday,'MUML': int(temp[0]),'MUMH': int(temp[1]),'DELL': int(temp[2]),'DELH': int(temp[3])}
      index = {'1'}
      test = pd.DataFrame(data = d ,index = index, columns=['sday','stime','eday', 'MUML', 'MUMH', 'DELL', 'DELH'])
      #print test


      #Features_train, Features_test, delay_train, delay_test = train_test_split(Features, delay,test_size=0.001)




      from sklearn.linear_model import LinearRegression
      regressor = LinearRegression()
      regressor.fit(Features, delay)

      delay_predictions = regressor.predict(test)
      Features_test = np.array([])
      #print type(np.asarray(Features_test))

      print int(delay_predictions)
      return int(delay_predictions)  
###############################################################################          
    

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()