import json
import requests
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")


def speaker(text):
    speak.Speak(text)


news = requests.get(
    "https://newsapi.org/v2/top-headlines?country=in&apiKey=d13e0e481a19496791ca17302442872c").text

news_dict = json.loads(news)

article = news_dict["articles"]


speaker("Hello")
speaker("I am your news reader bot")
speaker("let's start from today's indian headlines")

for i in article:
    speaker(i["title"])
    speaker(i["content"])
