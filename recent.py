import oppd
import codecs
import csv

papers = oppd.get_papers()
with codecs.open('recent.csv', 'w', 'utf-8') as recent_file:
	w = csv.writer(recent_file, delimiter=',')
	w.writerow(('title', 'type', 'link', 'tags', 'id'))
	w.writerows(map(
		lambda p: (p.title, p.link_type, p.link, ' '.join(p.tags), p.id),
		papers))
