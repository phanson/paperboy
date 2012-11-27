import twitter
import requests
import re
import itertools

_tag_pattern = '(?:(?<=\s)|^)#(\w*[A-Za-z0-9_\-]+\w*)'
_url_pattern = '(http://[a-zA-Z0-9_\-\%\./]+)'
_title_pattern = '"(.+)"'

class Paper:
	def __init__(self, id, text, tags, link, link_type, title):
		self.id = 0
		self.orig_tweet = text
		self.tags = tags
		self.link = link
		self.link_type = link_type
		self.title = title

def unshorten(url):
	r = requests.head(url)
	if not r.ok:
		raise Exception('Problem shortening URL')
	while r.status_code / 100 == 3:  # 300 series redirect from shortener
		url = r.headers['location']
		r = requests.head(url)
		if not r.ok:
			raise Exception('Problem shortening URL')
	return (r.url, r.headers['content-type'])

def get_papers():
	api = twitter.Api()
	statuses = api.GetUserTimeline('onepaperperday')
	papers = []
	for s in statuses:
		text = s.text
		tags = map(str, re.findall(_tag_pattern, text))
		urls = re.findall(_url_pattern, text)
		titles = re.findall(_title_pattern, text)
		for link in itertools.izip_longest(map(unshorten, urls), titles):
			papers.append(Paper(s.id, text, tags, link[0][0], link[0][1], link[1]))
	return papers
