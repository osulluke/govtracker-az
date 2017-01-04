import bs4, requests, subprocess

#open file of all the websites
websites = []
f = open('../data/links.txt', 'r')

#loop through all the websites gathering the basic html text, then insert each
#site into a list to gather page data from.
for filename in f:
    websites.append(filename)

for page in websites:
    print(page)

    #go get the data from each site
    res = requests.get(page)
    curl = subprocess.run(["curl", page])
    print(curl)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    links = soup.find_all('a')

    #gather links from each site and print them out
    for link in links:
        print(link.get('href'), link.text, sep = ' "', end='"\n')

# Go out on the web and get each page. Save each pages' source to disk:

#loop through the pages to gather 'hrefs', addresses, phone numbers, and email addresses.
