from selenium import webdriver
import datetime
from bs4 import BeautifulSoup
from lxml import html

today = str(datetime.datetime.now().date())

browser = webdriver.Chrome()

response = browser.get('http://na.op.gg/statistics/champion/')
html = browser.page_source
soupOPGG = BeautifulSoup(html, 'lxml')

#old way (not important, but keeping this right now)
# radio = browser.find_element_by_id("today")
# radio = browser.find_element_by_xpath(".//input[@type='radio' and @value='today']")
# test = radio.find_element_by_class_name('span')
# test.click()

# finds the button and all that I am pretty sure. But he problem is the click
# it is trying to clikc what I gave it, but the <span></span> is over the button and not allowing it to be pressed it seems
form = browser.find_element_by_xpath("//form[@id='statisticsChampionForm']")
radio = form.find_element_by_xpath("//input[@value='today']")
radio.click()

browser.quit()

anchor = soupOPGG.find('div', id='ChampionStatsTable')

# will find all information need from the initial page and hand it back
# for pos in anchor.find_all('tr', class_='Row'):
#     if(pos.find('td', class_='Cell Rank') != None):
#         champRank = pos.find('td', class_='Cell Rank').string
#         champNameAnchor = pos.find('td', class_='Cell ChampionName')
#         champName = champNameAnchor.find('a').string
#         champWinPercentage = pos.find('span', class_='Value').string
#         champGames = pos.find_all('td', class_='Cell')[4].string.strip()
#         print(champRank)
#         print(champName)
#         print(champWinPercentage)
#         print(champGames)
#         print()

