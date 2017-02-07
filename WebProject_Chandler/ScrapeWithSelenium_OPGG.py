from selenium import webdriver
import datetime
from bs4 import BeautifulSoup

today = str(datetime.datetime.now().date())

browser = webdriver.Chrome()

response = browser.get('http://na.op.gg/statistics/champion/')
html = browser.page_source
soupOPGG = BeautifulSoup(html, 'lxml')

browser.quit()

anchor = soupOPGG.find('div', id='ChampionStatsTable')

# will find all information need from the initial page and hand it back
for pos in anchor.find_all('tr', class_='Row'):
    if(pos.find('td', class_='Cell Rank') != None):
        champRank = pos.find('td', class_='Cell Rank').string
        champNameAnchor = pos.find('td', class_='Cell ChampionName')
        champName = champNameAnchor.find('a').string
        champWinPercentage = pos.find('span', class_='Value').string
        champGames = pos.find_all('td', class_='Cell')[4].string.strip()
        print(champRank)
        print(champName)
        print(champWinPercentage)
        print(champGames)
        print()

