import requests
from pathlib import Path

res = requests.get("https://autbor.com/example3.html")
res.raise_for_status()

# This script is useful for saving a full HTML page, which can then be parsed using bs4.

with open(
    "web-scraping/parsing-html-with-beautiful-soup/example3.html", "wb"
) as example_file:

    for chunk in res.iter_content(100_000):
        example_file.write(chunk)

isSaved = Path.exists("web-scraping/parsing-html-with-beautiful-soup/example3.html")
print(f"Saved: {isSaved}")
