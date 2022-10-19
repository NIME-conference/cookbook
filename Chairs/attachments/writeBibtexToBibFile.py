'''
- Implement script `paperDatabaseInterface.py`.  
- Implement and run script `scrapeBibtexFromPubpub.py`.  
- Update `YEAR` in this script.  
- Run this script.  
'''
YEAR = None     # e.g. "2021"
ADDRESS = None
MONTH = None    # e.g. "jun"

ARTICLE_NUMBER_STARTS_FROM = 1    # 0 | 1

import pickle
from typing import Dict

from paperDatabaseInterface import Paper, getAllPapers

def main():
    filename = 'bibtex_dict.pickle'
    print('Reading from', filename)
    with open(filename, 'rb') as f:
        bibtex_dict: Dict[int, str] = pickle.load(f)

    papers = [*getAllPapers()]
    papers.sort(key = lambda paper : paper.id)
    for i, paper in enumerate(papers):
        process(
            i + ARTICLE_NUMBER_STARTS_FROM, 
            paper, bibtex_dict[paper.id], 
        )

    # Here you may want to write back the updated `papers` to your database.  
    ...
    
    filename = f'nime{YEAR}.bib'
    print('Writing to', filename)
    with open(filename, 'w', encoding='utf-8') as f:
        for paper in papers:
            f.write(paper['bibtex'])
            f.write('\n\n')

def process(article_number: int, paper: Paper, bibtex: str):
    buffer = []
    fields = {}
    lines = bibtex.split('\n')
    line = lines.pop(0).strip()
    assert line.startswith('@inproceedings{')
    buffer.append('@inproceedings{NIME%s_%d,' % (YEAR[2:], article_number))
    for line in lines:
        if line == '}':
            continue
        key, value = line.split(' = ', 1)
        assert value.endswith(',')
        value = value[:-1]
        fields[key] = value
    authors = formatAuthors(paper.authors)
    if 'author' not in fields:
        fields['author'] = authors
        print(paper.id, 'missing authors. Guess:', authors)
    fields['booktitle'] = '{Proceedings of the International Conference on New Interfaces for Musical Expression}'
    fields['address'] = ADDRESS
    fields['issn'] = '{2220-4806}'
    fields['year'] = '{%s}' % YEAR
    fields['month'] = MONTH
    fields['article-number'] = '{%d}' % article_number
    fields['abstract'] = '{%s}' % (paper.abstract.replace('\u2028', '\n').replace('\u2029', '\n').replace('\n', ' '))
    if paper.video_url:
        fields['presentation-video'] = '{https://youtu.be/%s}' % paper.video_url
    for key in [
        'article-number', 
        'author', 'title', 'booktitle', 'year', 'month', 
        'address', 'issn', 'doi', 'url', 
        'presentation-video', 'abstract', 
    ]:
        try:
            buffer.append(f'  {key} = {fields[key]},')
        except KeyError:
            assert key == 'presentation-video'
    buffer[-1] = buffer[-1].rstrip(',')
    buffer.append('}')
    bibtex = '\n'.join(buffer)
    paper.bibtex = bibtex

def dotize(x: str):
    parts = x.split(' ')
    last = parts[-1]
    first = ' '.join(parts[:-1])
    return f'{last}, {first}'
def formatAuthors(authors):
    return '{' + ' and '.join([dotize(x) for x in authors]) + '}'

main()
