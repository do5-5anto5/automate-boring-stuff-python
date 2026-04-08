import requests

response = requests.get("https://automatetheboringstuff.com/files/rj.txt")
response.raise_for_status()

with open("Romeo and Juliet.txt", "wb") as play_file:
    # use 'wb' when saving requests response content — prevents file corruption

    # iter_content() method returns “chunks” of the content
    for chunk in response.iter_content(100_000):
        play_file.write(chunk)
