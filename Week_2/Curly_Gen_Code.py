import requests

headers = {
    'Authorization': 'Bearer ya29.A0ARrdaM-kuRsT9-fJMpj3qBr9h2gd8Oz1FupGMm1GlOS0fW0X5WgKewfI88c9N_vprGWdGWWN4zhLtlKNX3A0zIee5ZYHXBaQ8QeIh_p1QAPTDZXjPhalubmcKbEeuaAKUUOvwgafNiWgxwbmQlHQzPRfdnFV',
    'Accept': 'application/json',
}

params = (
    ('part', 'snippet, replies'),
    ('maxResults', '10'),
    ('order', 'time'),
    ('videoId', 'bVst_G7nhwU'),
    ('key', '[YOUR_API_KEY]'),
)

response = requests.get('https://youtube.googleapis.com/youtube/v3/commentThreads', headers=headers, params=params)

# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
#response = requests.get('https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet%2C%20replies&maxResults=10&order=time&videoId=bVst_G7nhwU&key=[YOUR_API_KEY]', headers=headers)

print(response)
print(response.json())