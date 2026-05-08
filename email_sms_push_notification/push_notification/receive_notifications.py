import requests, json

response = requests.get("https://ntfy.sh/some_subscribed_topic/json?poll=1")

notifications = []

for json_text in response.text.splitlines():
    notifications.append(json.loads(json_text))

for notification in notifications:
    print(notification['message'])
