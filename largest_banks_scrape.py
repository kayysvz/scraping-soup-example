from bs4 import BeautifulSoup as soup
import html5lib
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_banks?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork23455645-2022-01-01'
response = requests.get(url)

html_data = response.text

soup= soup(html_data, 'html.parser')


data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

tab = soup.find_all('tbody')[3].find_all('tr')
tab.pop(0)
name=[]
market=[]
for row in tab:
    name.append( row.find_all('a')[1].text)
    market.append( row.find_all('td')[2].text[:-4])

data['Name'] = name
data['Market Cap (US$ Billion)'] = market

data.to_json('largest_banks.json')
