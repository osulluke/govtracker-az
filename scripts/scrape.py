import bs4, requests #libraries for web-scraping

#variable set up
res = requests.get('https://codefortucson.github.io/govtracker-az/')
soup = bs4.BeautifulSoup(res.text,'html.parser')
links = soup.find_all('a')

#loop through data to pick out hypertext refs and name fields
for link in links:
    print(link.get('href'), sep=' ', end=' ')
