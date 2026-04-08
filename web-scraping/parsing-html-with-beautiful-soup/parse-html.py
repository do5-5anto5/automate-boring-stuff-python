# >>>import requests, bs4
# >>> res = requests.get('https://autbor.com/example3.html')
# >>> res.raise_for_status()
# >>> example_soup = bs4.BeautifulSoup(res.text, 'html.parser')
# >>> type(example_soup)
# <class 'bs4.BeautifulSoup'>

import bs4, requests

res = requests.get("https://autbor.com/example3.html")
res.raise_for_status()

# creating a BeautifulSoup object from a request response
example_soup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(example_soup))

# creating a BeautifulSoup object from local html file
with open(
    "web-scraping/parsing-html-with-beautiful-soup/example3.html"
) as example_file:
    example_soup_from_file = bs4.BeautifulSoup(example_file, "html.parser")
print(type(example_soup_from_file))
