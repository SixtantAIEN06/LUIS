import speech_recognition as sr
import requests
import json

def input_X_PhotoHub(text):
    response = requests.get(
        url=f'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/47fdbcf4-00cb-4e9a-a55c-df61cef1a102?verbose=true&timezoneOffset=0&subscription-key=7e25519a1e41462e8561a0bd60f5ddc2&q={text}'
    )
    if response.status_code != 200:
        print(f'status is not 200 ({response.status_code})')
        return
    # p = requests.Session()
    data = json.loads(response.text)
    print(text)
    intent = data['topScoringIntent']['intent']
    keyword = []
    _entity = len(data['entities'])
    for i in range(len(data['entities'])):
        keyword.append(data['entities'][i]['entity'])
    print(intent,keyword,_entity)

filename = "cat.wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data,language="zh-TW")

input_X_PhotoHub(text)
