import requests
from bs4 import BeautifulSoup

# Scrape APNewsBriefs with requests
urlOPGG = 'http://na.op.gg/statistics/champion/'
pageOPGG = requests.get(urlOPGG)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soupOPGG = BeautifulSoup(pageOPGG.content, 'lxml')

#gamesPlayed= list()
#for data in soupOPGG.find_all('tr', class_='Row Top'):
    #gamesPlayed.append(data.find('td', class_='Cell Rank').string)

#for position in soupOPGG.find_all('div', class_='ContentWrap'):
#    if(position.find('div', id='ChampionStatsTable') != None):
#        place1 = position.find('div', id="ChampionStatsTable")
        #place2 = place1.find('tbody', class_='Content')
        #testAnchor = place2.find('tr', class_='Row')
        #champRank = testAnchor.find('td', class_='Cell Rank').string
#        print(place1.find('tbody', class_='Content'))
#        print(place1)

print(soupOPGG.find_all('div', id='ChampionStatsTable'))
test = soupOPGG.find('div', id='ChampionStatsTable')
place = test.find('tr', class_='Row ')
print(place)

#print(soupOPGG.find_all('div', class_='ContentWrap'))

#position = soupOPGG.find_all('tbody', class_='Content')
#for position in soupOPGG.find_all('tbody', class_='Content'):
    #if(position.find('tr', class_='Row') != None):
        #anchor = position.find('tr', class_='Row')
        #champRank = anchor.find('td', class_='Cell Rank')
        #champName = anchor.find('td', class_='Cell ChampionName')
        #apOffice = brief.split(' (AP) ')[0]
        #fullStory = 'hosted.ap.org' + anchor.find('a').get('href')
        #ctime = fullStory.split('CTIME=')[1]

#print(gamesPlayed)

#print(position)
#print(anchor)
#print(champRank)
#print(champName)
#print(apOffice)
#print(fullStory)
#print(ctime)