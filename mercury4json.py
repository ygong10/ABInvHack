__author__ = 'ygong10'

import urllib2, json, sys, time, csv, re, requests

def main_loop():
     while 1:

        url = "https://server.alcoholanalytics.com/api/hackathon/?m=579&d=c&f=&l=&s=&t=j"
        response = urllib2.urlopen(url)
        data = json.load(response)

        with open('mercuryj.json', 'w') as outfile:
            print data
            json.dump(data, outfile)
        outfile.close

        time.sleep(0.1)

if __name__ == '__main__':
     try:
         main_loop()
     except KeyboardInterrupt:
         print >> sys.stderr, '\nExiting by user request.\n'
         sys.exit(0)