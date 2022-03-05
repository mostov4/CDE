import requests

headers = {
    'Authorization': 'Bearer ya29.A0ARrdaM-kuRsT9-fJMpj3qBr9h2gd8Oz1FupGMm1GlOS0fW0X5WgKewfI88c9N_vprGWdGWWN4zhLtlKNX3A0zIee5ZYHXBaQ8QeIh_p1QAPTDZXjPhalubmcKbEeuaAKUUOvwgafNiWgxwbmQlHQzPRfdnFV',
    'Accept': 'application/json',
}

params = (
    ('part', 'snippet'),
    ('key', '[YOUR_API_KEY]'),
)

json_data = {
    'snippet': {
        'videoId': 'TOp2Co4XKRc',
        'topLevelComment': {
            'snippet': {
                'textOriginal': 'You the best',
            },
        },
    },
}

response = requests.post('https://youtube.googleapis.com/youtube/v3/commentThreads', headers=headers, params=params, json=json_data)

# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
#response = requests.post('https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet&key=[YOUR_API_KEY]', headers=headers, json=json_data)