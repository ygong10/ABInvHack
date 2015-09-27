__author__ = 'ygong10'
import urllib2, requests, re, csv
from bs4 import BeautifulSoup

url = "http://www.nhl.com/ice/schedulebyweek.htm"
r = requests.get(url)
data=r.text
soup = BeautifulSoup(data)

dates =[]
two_teams = []
teams = []
first_team = []
second_team = []
location = []
untrimmed_time=[]
trim_time = []
years = []
months = []
days = []
readable_date = []

for table in soup.find_all('table', {'class':'data schedTbl'}):
    for tr in table.find_all('tr', {'class':'preseason'}):

        for date in tr.find_all('td', {'class':'date'}):
            for start_date in date.find_all('div', {'class':'skedStartDateSite'}):
                #print(start_date.text)
                dates.append(start_date.text)

        for team in tr.find_all('td', {'class':'team'}):
            for team_name in team.find_all('div', {'class':'teamName'}):
                for link in team.find_all('a', {'href':'javascript:void(0);'}):
                   #print(link.text)
                   two_teams.append(link.text)

        for time in tr.find_all('td', {'class':'time'}):
            for start_time in time.find_all('div', {'skedStartTimeEST'}):
                #print(start_time.text)
                untrimmed_time.append(start_time.text)

for i in range(len(dates)):
    if "Sep" in dates[i]:
        months.append(9)
        #print(dates[i])
    if "Oct" in dates[i]:
        months.append(10)

    day_line = re.search("([\d]{1,2})", dates[i])
    days.append(day_line.group(0))
    #print(day_line.group(0))

    years_line = re.search("[.*^\d{2}](\d{1})$", dates[i])
    years.append(years_line.group(0))
    #print(years[i])

for i in range(len(two_teams)):
    if i%2!=0:
        teams.append(two_teams[i])
        #print(two_teams[i])
for i in range(len(teams)):
    if i%2==0:
        first_team.append(teams[i])
        #print(teams[i])
    else:
        second_team.append(teams[i])
        location.append(teams[i])
        #print(teams[i])

for i in range(len(untrimmed_time)):
     line= re.sub('[ET]','',untrimmed_time[i])
     trim_time.append(line)
     #print(trim_time[i])


lines = []
for i in range(len(dates)):
    begin_time = (str(months[i]) + "/" + str(days[i]) + "/" + str(years[i]))
    # line = (first_team[i] + " vs " + second_team[i] + "," + begin_time + ", FALSE ," + trim_time[i] + ", ," + location[i] + ", ").encode('utf-8').strip()
    #line = (first_team[i], " vs " + second_team[i] + "," + begin_time + ", FALSE ," + trim_time[i] + ", ," + location[i] + ", ")
    lines.append(line)
    print lines[i]

#header = "Subject, Start Date, All Day Event, Start Time, End Time, Location, Description"
with open("sports_data.csv", 'wb') as outfile:
    wr = csv.writer(outfile, delimiter=',',quoting=csv.QUOTE_ALL)
    wr.writerow(["Subject", "Start Date", "All Day Event", "Start Time", "End Time", "Location", "Description"])
    for i in range(len(dates)):
         begin_time = (str(months[i]) + "/" + str(days[i]) + "/" + str(years[i]))
         wr.writerow([first_team[i].encode('utf-8') + " vs " + second_team[i].encode('utf-8'), begin_time, "FALSE", trim_time[i], "", location[i].encode('utf-8'), ""])
         print([first_team[i].encode('utf-8') + " vs " + second_team[i].encode('utf-8'), begin_time, "FALSE", trim_time[i], "", location[i].encode('utf-8'), ""])






