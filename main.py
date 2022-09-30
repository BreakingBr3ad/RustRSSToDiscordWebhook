import os
from dotenv import load_dotenv
import feedparser
import requests
import time
load_dotenv()
webhookUrl = os.environ['webhookUrl']
oldwebhook = ''
while True:
  RustFeed = feedparser.parse("https://rust.facepunch.com/rss/news")
  webhookBody = {'content': f"{RustFeed.entries[0].id}"}
  if oldwebhook != webhookBody:
    oldwebhook = webhookBody
    webhookReq = requests.post(webhookUrl, data=webhookBody)
  time.sleep(1700)
