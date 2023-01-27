import requests
import json
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")


news = requests.get(
    "https://newsapi.org/v2/top-headlines?country=in&apiKey=d13e0e481a19496791ca17302442872c").text


dic = json.loads(news)

arts = dic["articles"]


for i in arts:
    speak.Speak(i['title'])
    speak.Speak(i['content'])
