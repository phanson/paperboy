import codecs
import csv

def to_html(papers, filename):
	with codecs.open(filename, 'w', 'utf-8') as html:
		html.write("<!DOCTYPE html><html><head><title>One Paper A Day</title></head><body><ul>")
		first = True
		for paper in papers:
			if first:
				first = False
				continue
			html.write('<li><a href="%s">%s</a> (%s)</li>' % (paper[2], paper[0], paper[1]))
		html.write("</ul></body></html>")

with codecs.open('recent.csv', 'r', 'utf-8') as recent_file:
	papers = csv.reader(recent_file, delimiter=',')
	to_html(papers, 'recent.htm')
