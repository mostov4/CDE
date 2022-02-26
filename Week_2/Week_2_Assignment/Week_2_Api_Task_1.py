import requests

url = "https://api.aniapi.com/v1/anime/"

payload={}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEyNTciLCJuYmYiOjE2NDU4NjU1MzgsImV4cCI6MTY0ODQ1NzUzOCwiaWF0IjoxNjQ1ODY1NTM4fQ.kJfCTh6ixmerh54jPQqT4H-BAgi7EoTa5PN-t0-oPKI'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)