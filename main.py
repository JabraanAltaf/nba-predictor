# Program: Gets my predictions for today's game and then gives me a output of my results in the morning
# API - Use NBA API to get current day's games 
# Stores my predictions for results and tracks my record overtime -> use some visualisation tool? 
# Design Image: draw.draw.io file stored locally

import requests, json 
from datetime import date
import csv

def get_date():
    # Today's date
    today = date.today()

    # Get data in YMD format and cast as Int
    int_date = int(today.strftime("%Y%m%d"))

    return int_date

def get_schedule(int_date):     
    # URL
    url = requests.get(("https://data.nba.net/10s/prod/v1/{}/scoreboard.json").format(int_date))
    text = url.text

    #Load in data as JSON
    data = json.loads(text)

    #print(data)
    for i in range (len(data['games'])):
        print ("------------------------------------")
        print(data['games'][i]['vTeam']['triCode'], data['games'][i]['hTeam']['triCode'])
       # print(data['games'][i]['vTeam']['win']) 
       # print(data['games'][i]['vTeam']['loss']) 
       # print("\n@\n")
       # print(data['games'][i]['hTeam']['triCode']) 
       # print(data['games'][i]['hTeam']['win']) 
       # print(data['games'][i]['hTeam']['loss']) 

    return data

def write_matchups_csv(int_date, data):
    headers = ['Home','Away', 'homeW',"homeL", "awayW", "awayL"]
   # data = json.loads(requests.get("https://data.nba.net/10s/prod/v1/20220302/scoreboard.json").text)
    #with urllib.request.urlopen("https://data.nba.net/10s/prod/v1/20220302/scoreboard.json") as url:
    #data = json.loads(url.read().decode())


    filename = 'nba-{}.csv'.format(int_date)
    #print(len(data['games']))
    with open(filename, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header

        writer.writerow(headers)

        # write the data
      #  writer.writerow(data)

def main():
    date = get_date()
    schedule_data = get_schedule(date)
    #write_matchups_csv(date, schedule_data)

main()