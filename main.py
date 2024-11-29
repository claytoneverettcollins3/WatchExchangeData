import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the website
url = "https://old.reddit.com/r/Watchexchange/search/?q=watchexchange&sort=top&restrict_sr=on&t=year"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

elements = soup.select('.search-title.may-blank')

titles = [element.text for element in elements]

df = pd.DataFrame(titles, columns=['Post_Title'])

print(df)
