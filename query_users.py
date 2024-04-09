# query_users.py
import requests

response = requests.get('http://localhost:5000/api/users')
if response.status_code == 200:
    users = response.json()
    for user in users:
        print(f"Username: {user['username']}, Email: {user['email']}")
else:
    print("Failed to retrieve user data.")
