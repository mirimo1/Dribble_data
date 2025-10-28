import requests

url = "http://127.0.0.1:8000/api/games/"

game_data = {
    "date": "2025-10-27",
    "home_team": "Lakers",
    "away_team": "Warriors",
    "home_score": 112,
    "away_score": 108
}

response = requests.post(url, json=game_data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())