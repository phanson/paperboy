import onepaperperday
from onepaperperday import serialize
import codecs

papers = onepaperperday.get_papers()
with codecs.open('papers.csv', 'w', 'utf-8') as recent_file:
	serialize.to_csv(papers, recent_file)
