import requests
import json

url = "https://api.github.com/user"

payload={}
headers = {
  'Authorization': 'Bearer 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',
  'Cookie': '_octo=GH1.1.1397917353.1645263806; logged_in=no'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response) #gives 200 code for successful
print(response.text)

json_string = response.text
data = json.loads(json_string)
print(len(data))

print(type(data))

