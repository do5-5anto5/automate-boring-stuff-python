import requests, bs4, time


def get_comics(url: str, max_down: int):
    
    """
    Downloads all comics from xkcd.com up to max_down number of pages.
    
    Parameters:
    url (str): URL of the first comic page to download
    max_down (int): Number of pages to download
    
    Returns:
    None
    
    Raises:
    requests.exceptions.RequestException: If there is an issue with getting the image.
    """
    path = str(url)
    count = int(max_down)

    if count == 0:
        return

    response = requests.get(path)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    comic_src = soup.select("#comic img")

    if comic_src:
        try:
            src = comic_src[0].attrs["src"]

            comic_res = requests.get(f"https:{src}")
            comic_res.raise_for_status()

            filename = src.split("/")[-1]

            with open(
                f"exercises/web-scraping/downloadXKCD-comics/comic-{filename}", "wb"
            ) as comic:
                for chunk in comic_res.iter_content(100_000):
                    comic.write(chunk)
                    time.sleep(0.5)
        except requests.exceptions.RequestException as e:
            print(f"file to download image: {e}")
    else:
        print(f"No image at {url}")

    prev_elem = soup.select(".comicNav a")[1].attrs["href"]

    count -= 1
    get_comics(f"https://xkcd.com/{prev_elem}", count)

get_comics(url = "https://xkcd.com", max_down= 5)
