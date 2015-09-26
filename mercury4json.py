__author__ = 'ygong10'

import urllib2, json, sys, time, csv, re, requests

def main_loop():
     while 1:

         url = "https://server.alcoholanalytics.com/api/hackathon/?m=579&d=c&f=&l=&s=&t=j"
         response = urllib2.urlopen(url)
         data = json.load(response)



        # csvfile = open('mercuryc.csv', 'r')
        # jsonfile = open('mercuryj.json', 'w')
        #
        # #fieldnames = ("FirstName","LastName","IDNumber","Message")
        # reader = csv.reader(csvfile)
        # for row in reader:
        #     json.dump(row, jsonfile)
        #     jsonfile.write('\n')
        #     print row

         with open("mercuryj.json", "wb") as outfile:
             for row in data:
                json.dump(row, outfile)
                outfile.write("\n")
                print row

         time.sleep(0.1)

if __name__ == '__main__':
     try:
         main_loop()
     except KeyboardInterrupt:
         print >> sys.stderr, '\nExiting by user request.\n'
         sys.exit(0)