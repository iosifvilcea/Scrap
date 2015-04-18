import requests
import re
from newspaper import Article
from lxml import html
from bs4 import BeautifulSoup

article_websites = ["www.techcrunch.com"]
article_url_re = re.compile('http://techcrunch\.com/20[0-9][0-9]/[0-1][0-9]/[0-3][0-9]/.*')
#article_comment_re = re.compile('http://techcrunch\.com/20[0-9][0-9]/[0-1][0-9]/[0-3][0-9]/.*/#comments')

articles = []



for site in article_websites:
	r = requests.get("http://" + site)
	data = r.text

	soup = BeautifulSoup(data)
	for link in soup.find_all('a'):
		article_link = link.get('href')
		try:
			if article_url_re.match(article_link):
				if article_link not in articles and not article_link.endswith('#comments'):
					articles.append(article_link)
					# print article_link
		except AttributeError as ae:
			print str(ae)
		except TypeError as te:
			print str(te)


for article in articles:
	a = Article(article)
	a.download()
	a.parse()
	# print a.title
	a.nlp()
	print a.keywords





		