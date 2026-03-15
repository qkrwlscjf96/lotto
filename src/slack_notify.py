import requests

SLACK_URL="YOUR_WEBHOOK"

def send_slack(msg):

    payload={"text":msg}

    requests.post(SLACK_URL,json=payload)
