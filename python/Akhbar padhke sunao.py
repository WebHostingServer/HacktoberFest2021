import json
import requests

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

# speak("News for today")

if __name__=='__main__':
    # speak("News for today")
    url="http://newsapi.org/v2/top-headlines?country=in&apiKey=47c2ca33ecd24419b753c88a9df9330d"
    r=requests.get(url).text
    # print(r)
    data=json.loads(r)
    print(data["articles"])
    arts=(data["articles"])
    # for article in arts:
    #     speak(article['title'])
    #     speak("Next news is")
    for i in arts:
        speak(i["title"])
        speak("Next news is")

