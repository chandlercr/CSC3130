
# I NEED TO REWORK THIS for both pick and ban

from selenium import webdriver
import datetime
from bs4 import BeautifulSoup
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create list of dicts for JSON Object
response = []

# Prepare for parsing with BeautifulSoup
browser = webdriver.Chrome('/Users/ChandlerCapps/anaconda/bin/chromedriver')
urlResponse = browser.get('http://na.op.gg/statistics/champion/')
urlResponse = browser.find_element_by_class_name('StatisticsFilter').find_element_by_class_name('Content').find_elements_by_class_name('Cell')[2].find_elements_by_class_name('RadioButton')[2].find_element_by_class_name('Label').click()
urlResponse = browser.find_element_by_class_name('StatisticsFilter').find_element_by_class_name('Content').find_elements_by_class_name('Cell')[0].find_elements_by_class_name('RadioButton')[3].find_element_by_class_name('Label').click()


# Wait until the element shows on the Browser after the click
try:
    element = WebDriverWait(browser, 30).until(
        # Waits for the informtion to show up rather than the table
        EC.presence_of_element_located((By.XPATH, '//*[@id="ChampionStatsTable"]/table/tbody/tr[1]'))
    )
finally:
    html = browser.page_source
    soupOPGG = BeautifulSoup(html, 'lxml')
    browser.quit()

anchor = soupOPGG.find('div', id='ChampionStatsTable')
today = str(datetime.datetime.now().date())

# Parse url
# this is for "Win percentage" based results
for pos in anchor.find_all('tr', class_='Row'):
    if(pos.find('td', class_='Cell Rank') != None):
        champRank = pos.find('td', class_='Cell Rank').string
        champNameAnchor = pos.find('td', class_='Cell ChampionName')
        champName = champNameAnchor.find('a').string
        champBanRate = pos.find('span', class_='Value').string

        # Make changes to response
        response.append({'Champion_Name': champName, 'Champion_Rank': champRank, 'Champion_BanRate': champBanRate, 'Date_Scraped': today})


# Write response to JSON file
postingsFile = '/Users/ChandlerCapps/Desktop/CSC3130/WebProject_Chandler/JSON/OPGG/Daily_Ban/' + today + 'Ban_Ratio.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
