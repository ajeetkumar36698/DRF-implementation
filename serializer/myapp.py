import requests
URL="http://127.0.0.1:8000/student/1"
r=requests.get(url=URL)
json_data=r.json()
print(json_data)