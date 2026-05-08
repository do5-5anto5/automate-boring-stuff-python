import requests

requests.post(
    "https://ntfy.sh/some_subscribed_topic",
    "The rent is too high!",
    headers={
        "Title": "Important: Read this!",
        "Tags": "warning,neutral_face",
        "Priority": "5",
    },
)
