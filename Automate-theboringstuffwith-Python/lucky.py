#! python3
# lucky.py

import webbrowser, sys, requests, bs4

# Read command line arguments from sys.argv
print ('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Fetch search results page with requests module
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Find links to each search result
linkElems = soup.select('.r a')

# Call webbrowser.open() function
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))