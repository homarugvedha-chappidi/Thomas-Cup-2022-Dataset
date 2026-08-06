import requests
import json

url = "https://extranet-lv.bwfbadminton.com/api/tournaments/draw/players"

params = {
    "tournament_id": 4592,
    "draw_code": 5
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)

try:
    data = response.json()
    print(json.dumps(data, indent=4))
except Exception as e:
    print("Error:", e)
    print(response.text)
