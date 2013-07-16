import twitter
import requests
import re
import itertools
from urlparse import urlparse
import urllib

_tag_pattern = '(?:(?<=\s)|^)#(\w*[A-Za-z0-9_\-]+\w*)'
_url_pattern = '(https?://[a-zA-Z0-9_\-\%\./]+)'
_title_pattern = '"(.+)"'


class Paper:
	def __init__(self, id, text, tags, link, link_type, title):
		self.id = id
		self.orig_tweet = text
		self.tags = tags
		self.link = link
		self.link_type = link_type
		if title:
			self.title = title.strip()
		else:
			self.title = urllib.unquote_plus('.'.join(urlparse(link).path.split('/')[-1].split('.')[:-1])).strip()


def unshorten(url):
	r = requests.head(url)
	if not r.ok:
		return (url, '')
	while r.status_code / 100 == 3:  # 300 series redirect from shortener
		url = r.headers['location']
		try:
			r = requests.head(url)
		except:
			return (url, '')
		if not r.ok:
			return (url, '')
	return (r.url, r.headers['content-type'])


def get_papers(keys):
	api = twitter.Api(**keys)
	statuses = api.GetUserTimeline(screen_name='onepaperperday')
	papers = []
	for s in statuses:
		text = s.text
		tags = map(str, re.findall(_tag_pattern, text))
		urls = re.findall(_url_pattern, text)
		titles = re.findall(_title_pattern, text)
		for link in itertools.izip_longest(map(unshorten, urls), titles):
			if link[0] is not None:
				papers.append(Paper(s.id, text, tags, link[0][0], link[0][1].split(';')[0], link[1]))
	return papers
