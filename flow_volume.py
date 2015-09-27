__author__ = 'ygong10'

import urllib2, json, sys, time, csv, re, requests

def main_loop():
     while 1:

        url = "https://server.alcoholanalytics.com/api/hackathon/?m=579&d=c&f=&l=&s=&t=c"
        response = urllib2.urlopen(url)
        data = csv.reader(response)

        with open('volumec.csv', 'wb') as outfile:
            wr = csv.writer(outfile, delimiter=',',quoting=csv.QUOTE_ALL)
            for row in data:
                wr.writerow(row)
                print row

        time.sleep(0.1)

if __name__ == '__main__':
     try:
         main_loop()
     except KeyboardInterrupt:
         print >> sys.stderr, '\nExiting by user request.\n'
         sys.exit(0)