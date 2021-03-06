# Program: Gets my predictions for today's game and then gives me a output of my results in the morning
# API - Use NBA API to get current day's games 
# Stores my predictions for results and tracks my record overtime -> use some visualisation tool? 
# Design Image: draw.draw.io file stored locally

import requests, json 
from datetime import date
import csv
import pandas as pd

def get_date():
    # Today's date
    today = date.today()
    # Get data in YMD format and cast as Int
    int_date = int(today.strftime("%Y%m%d"))
    
    return int_date

def get_schedule(int_date):     
    Home = []
    Away = []
    # HomeWs
    Hw = []
    Hl = []
    # AwayWs
    Aw = []
    Al = []


    # URL
    url = requests.get(("https://data.nba.net/10s/prod/v1/{}/scoreboard.json").format(int_date))
    text = url.text

    #Load in data as JSON
    data = json.loads(text)

    #print(data)
    for i in range (len(data['games'])):
        Home.append(data['games'][i]['hTeam']['triCode'])
        Away.append(data['games'][i]['vTeam']['triCode'])
        # Getting Home Team's Win % 
        HomeWins = int(data['games'][i]['hTeam']['win'])
        AwayWins = int(data['games'][i]['vTeam']['win'])

        HomeLoss = int(data['games'][i]['hTeam']['loss'])
        AwayLoss = int(data['games'][i]['vTeam']['loss'])
        #HomeW = round(int(data['games'][i]['hTeam']['win'])/(int(data['games'][i]['hTeam']['loss'])+int(data['games'][i]['hTeam']['win'])) * 100, 2)
        # Getting Away Team's Win %
       # AwayW = round(int(data['games'][i]['vTeam']['win'])/(int(data['games'][i]['vTeam']['loss'])+int(data['games'][i]['vTeam']['win'])) * 100, 2)

        Hw.append(HomeWins)
        Aw.append(AwayWins)

        Hl.append(HomeLoss)
        Al.append(AwayLoss)
    #Create dictionary
    dict = {'Home': Home,'HomeW': Hw, 'HomeL': Hl,'Away': Away, 'AwayW': Aw, 'AwayL': Al} 


    return dict


def write_matchups_csv(int_date, dict):

    df = pd.DataFrame(dict, index=None)
    filename = 'nba-{}.csv'.format(int_date)
    df.to_csv(filename) 


def main():
    date = get_date()
    schedule_data = get_schedule(date)
    write_matchups_csv(date, schedule_data)

main()