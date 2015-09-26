__author__ = 'ygong10'

import urllib2, json, sys, time, re, requests

def main_loop():
     while 1:
#while True:
        url = "https://server.alcoholanalytics.com/api/hackathon/?m=579&d=c&f=&l=&s=&t=j"
        response = urllib2.urlopen(url)
        data = json.loads(response.read())
                #above_ID =  data[0]['id']
        print data

        with open('non_real_time_data.txt', 'w') as outfile:
            json.dump(data, outfile)
        outfile.close
        time.sleep(0.1)

if __name__ == '__main__':
     try:
         main_loop()
     except KeyboardInterrupt:
         print >> sys.stderr, '\nExiting by user request.\n'
         sys.exit(0)