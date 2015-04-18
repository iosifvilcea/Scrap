from newspaper import Article
from lxml import html
import requests
from bs4 import BeautifulSoup

article_websites = ["www.techcrunch.com"]

for site in article_websites:
	r = requests.get("http://" + site)
	data = r.text

	soup = BeautifulSoup(data)
	for link in soup.find_all('a'):
		print link.get('href')
		