import requests, webbrowser, bs4, time

def open_book_pages():
    """
    Opens the first 5 books from the books.toscrape.com website in the default browser.

    This function sends a GET request to the website, parses the HTML received with
    BeautifulSoup, searches for the book links pattern, and opens the first 5 books in
    the default browser with a 0.5 second delay between each.
    """
    print("Searching...")

    response = requests.get(f"https://books.toscrape.com/")
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    books = soup.select("article.product_pod h3 > a")

    for index in range(5):
        book_ref = str(books[index].attrs["href"])
        webbrowser.open(f"https://books.toscrape.com/{book_ref}")
        time.sleep(0.5) # avoid fast requests


open_book_pages()
