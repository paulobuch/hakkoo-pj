import requests

access_token = 'YOUR_ACCESS_TOKEN'
profile_url = f'https://graph.instagram.com/me?fields=id,username&access_token={access_token}'

response = requests.get(profile_url)
profile_data = response.json()

print(profile_data)