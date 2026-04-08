import requests

response = requests.get("https://automatetheboringstuff.com/files/rj.txt")

if response.status_code == requests.codes.ok:
    print(f"Status: OK {response.status_code}")
    print(f"Text lengh: {len(response.text)}")
    print(f"{response.text[:329]}")
