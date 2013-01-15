import csv

def to_html(papers, stream):
	stream.write('<ul>')
	for paper in papers:
		stream.write('<li><a href="%s">%s</a> (%s)</li>' % (paper.link, paper.title, paper.link_type))
	stream.write('</ul>')

def to_csv(papers, stream):
	w = csv.writer(stream, delimiter=',')
	w.writerow(('title', 'type', 'link', 'tags', 'id'))
	w.writerows(map(
		lambda p: (p.title, p.link_type, p.link, ' '.join(p.tags), p.id),
		papers))
