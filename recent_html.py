import onepaperperday
from onepaperperday import serialize
import codecs

papers = onepaperperday.get_papers()
with codecs.open('papers.htm', 'w', 'utf-8') as html_file:
	html_file.write('<html><head><title>One Paper Per Day</title></head><body><h1>One Paper Per Day</h1>')
	serialize.to_html(papers, html_file)
	html_file.write('</body></html>')
