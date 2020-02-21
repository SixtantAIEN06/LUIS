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
    intent = data['topScoringIntent']['intent']
    keyword = []
    _entities = len(data['entities'])
    for i in range(len(data['entities'])):
        keyword.append(data['entities'][i]['entity'])
    print(intent,keyword,_entities)

# type = input("輸入搜尋方式(1.打字 2.語音)：")
# if type == '1' :
#     text = input('請輸入搜尋關鍵字:');
#     input_X_PhotoHub(text);
# elif type == '2' :
#     recognizer = sr.Recognizer();
#     microphone = sr.Microphone();
#     with microphone as source:
#         print('請說出搜尋關鍵字：');
#         recognizer.adjust_for_ambient_noise(source);
#         audio = recognizer.listen(source);
#     try:
#         text=recognizer.recognize_google(audio, language='zh-tw');
#         input_X_PhotoHub(text);
#     except:
#         pass
# else :
#     print('輸入錯誤！！')
text = input("請輸入搜尋關鍵字:\n" )
input_X_PhotoHub(text)