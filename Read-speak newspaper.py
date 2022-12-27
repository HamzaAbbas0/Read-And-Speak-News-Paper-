import json

from win32com.client import Dispatch
import requests

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    result=speak.speak(str)


if __name__ == '__main__':
    speak("Hello Welcome To the Hamza Abbas News Channel Our today news are")
    url = "https://newsapi.org/v2/top-headlines/sources?apiKey=558d5c5b597c40d2b87051e32852fbe5"
    news = requests.get(url).text
    newsjson = json.loads(news)
    articles =(newsjson["sources"])
    for index,arts in enumerate(articles):
        results=(arts["description"])
        resultss=(arts["url"])
        print(index)
        print(results)
        speak(results)
        print(resultss)
        if index == 3:
            speak("our today last news are")


        if index ==4:
            # speak(results)
            speak("thanks for watching the hamza abbas news channel")
            break





