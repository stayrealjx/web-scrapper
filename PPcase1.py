from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.entrepreneur.com/article/242702'

# opening up connection, grabbing the page
uClient = uReq(my_url)
# close the file
uClient.close()

page_html = uClient.read()
page_soup = soup(page_html, "html.parser")

records = []
for result in results:
    company_name = result.find('a').text
    location = result.contents[2]
    location = location[1:]
    official_website = result.find('a')['href']
    records.append((company_name, location, official_website))
    
import pandas as pd
df = pd.DataFrame(records, columns=['company_name', 'location', 'official_website'])
df.head()

df.to_csv('PPcase1.csv', index=False, encoding='utf-8')
df = pd.read_csv('PPcase1.csv', encoding='utf-8')