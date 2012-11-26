import twitter
import re
import itertools

_tag_pattern = '(?:(?<=\s)|^)#(\w*[A-Za-z0-9_\-]+\w*)'
_url_pattern = '(http://[a-zA-Z0-9_\-\%\./]+)'
_title_pattern = '"(.+)"'

class Paper:
	tags = []
	orig_tweet = ''
	title = None
	link = ''
	link_type = None
	
	def __init__(self, text, tags, link, link_type, title):
		self.orig_tweet = text
		self.tags = tags
		self.link = link
		self.link_type = link_type
		self.title = title

def unshorten(url):
	return url

def get_link_type(url):
	return None

api = twitter.Api()
statuses = api.GetUserTimeline('onepaperperday')
papers = []
for s in statuses:
	text = s.text
	tags = map(str, re.findall(_tag_pattern, text))
	urls = re.findall(_url_pattern, text)
	titles = re.findall(_title_pattern, text)
	for link in itertools.izip_longest(map(unshorten, urls), titles):
		papers.append(Paper(text, tags, link[0], get_link_type(link[0]), link[1]))

for p in papers:
	if p.title:
		print '"%s" %s %s' % (p.title.strip(), repr(p.tags), p.link)
	else:
		print '(no title) %s %s' % (repr(p.tags), p.link)
