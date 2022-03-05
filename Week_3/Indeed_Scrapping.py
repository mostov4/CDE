from cgitb import text
import requests
from bs4 import BeautifulSoup

url = "https://bagallery.com/collections/framesi-morphosis"

response = requests.get(url=url)
response.text

soup = BeautifulSoup(response.text,'html.parser')

job_name = soup.select_one('div.grid-item div.product-bottom a.product-title')
print(len(job_name))

job_name_all = soup.select('div.grid-item div.product-bottom a.product-title')
print(len(job_name_all))

