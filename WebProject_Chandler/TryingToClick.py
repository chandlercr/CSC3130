from selenium import webdriver
import datetime
from bs4 import BeautifulSoup
from lxml import html
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

today = str(datetime.datetime.now().date())

browser = webdriver.Chrome()
response = browser.get('http://na.op.gg/statistics/champion/')
response = browser.find_element_by_class_name('StatisticsFilter').find_element_by_class_name('Content').find_elements_by_class_name('Cell')[2].find_elements_by_class_name('RadioButton')[2].find_element_by_class_name('Label').click()

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "ChampionStatsTable"))
    )
finally:
    html = browser.page_source
    soupOPGG = BeautifulSoup(html, 'lxml')
    # print(html)
    browser.quit()


anchor = soupOPGG.find('div', id='ChampionStatsTable')

# Scraping Code:
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