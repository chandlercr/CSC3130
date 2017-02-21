from selenium import webdriver
import datetime
from bs4 import BeautifulSoup
import json

# Create list of dicts for JSON Object
response = []

# Prepare for parsing with BeautifulSoup
browser = webdriver.Chrome('/Users/ChandlerCapps/anaconda/bin/chromedriver')
urlResponse = browser.get('http://na.op.gg/statistics/champion/')
html = browser.page_source
soupOPGG = BeautifulSoup(html, 'lxml')
browser.quit()
anchor = soupOPGG.find('div', id='ChampionStatsTable')

# Parse url
# this is for "Win percentage" based results
for pos in anchor.find_all('tr', class_='Row'):
    if(pos.find('td', class_='Cell Rank') != None):
        champRank = pos.find('td', class_='Cell Rank').string
        champNameAnchor = pos.find('td', class_='Cell ChampionName')
        champName = champNameAnchor.find('a').string
        champWinPercentage = pos.find('span', class_='Value').string
        champGames = pos.find_all('td', class_='Cell')[4].string.strip()

        # Make changes to response
        response.append({'Champion Name': champName, 'Champion Rank': champRank, 'Win Percentage': champWinPercentage, 'Number of Games': champGames})

# Write response to JSON file
today = str(datetime.datetime.now().date())
postingsFile = '/Users/ChandlerCapps/Desktop/CSC3130/WebProject_Chandler/JSON/' + today + '_OPGG_WinPercentage.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
