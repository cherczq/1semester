import requests
from bs4 import BeautifulSoup
url = "https://example.com/blog"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")