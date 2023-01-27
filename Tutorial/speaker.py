from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")


speak.Speak("Is cos sqare x periodic")
