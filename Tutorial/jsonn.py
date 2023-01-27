import json
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")


# dumps takes dictionary and gives String
# loads takes string and gives dictionary

details = {

    "Name": "Aritra",
    "Roll": 81,
    "Foods": ["Biriyani", "Butter naan", "Tandoori Chicken"],
    "lang": ("C", "Python", "HTML"),

}

text = '{"Aritra":81,"Soumodip":89,"Jotisman":39}'


dic = json.loads(text)

for i in dic.items():
    speak.Speak(i)
