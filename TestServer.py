''' 
_*_ coding: utf-8 _*_
Date: 2022/3/4
Author: 
Intent:
'''

import requests
import json

def test_api(text, out):
    #url = "http://127.0.0.1:10001/TextToSpeech"
    url = "http://127.0.0.1:9080/synthesize"
    data = {
        "text": "床前明月光，疑是地上霜。举头望明月，低头思故乡。", 
        "out": "test.wav",
        "speaker":"Azusa",
        "model":["logs/azusa/G_2800.pth","logs/azusa/config.json"],
        "lang":"[ZH]"
    }
    print(type(data))
    json_data = json.dumps(data)
    print(type(json_data))
    headers = {"Content-Type": "application/json"}
    res = requests.post(url, data=json_data, headers=headers)
    print(res)
    return res

if __name__ == "__main__":
    text = "踢足球的人"
    out = "tmp.wav"
    test_api(text, out)

    pass
