import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"
data = {
    'name':'Mansi Gupta',
    'roll':103,
    'city':'Gola'
}
json_data=json.dumps(data) #convert data  into json
r = requests.post(url=URL,data=json_data)

newdata=r.json()
print('response: ',newdata)