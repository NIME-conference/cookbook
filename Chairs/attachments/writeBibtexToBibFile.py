'''
You may refer to the doc string of `scrapeBibtexFromPubpub.py`
then, update `YEAR`. 
'''
YEAR = None     # e.g. "2021"
ADDRESS = None
MONTH = None    # e.g. "jun"

import pickle

def main():
    filename = 'withChannels.pickle'
    print('Reading from', filename)
    with open(filename, 'rb') as f:
        papers = pickle.load(f)

    filename = 'bibtex_dict.pickle'
    print('Reading from', filename)
    with open(filename, 'rb') as f:
        bibtex_dict = pickle.load(f)

    papers.sort(key = lambda x : x['paper_id'])
    for i, paper in enumerate(papers):
        paper_id = paper['paper_id']
        process(i + 1, paper_id, paper, bibtex_dict[paper_id])

    filename = 'ready.pickle'
    print('Writing to', filename)
    with open(filename, 'wb') as f:
        pickle.dump(papers, f)
    
    filename = f'nime{YEAR}.bib'
    print('Writing to', filename)
    with open(filename, 'w', encoding='utf-8') as f:
        for paper in papers:
            f.write(paper['bibtex'])
            f.write('\n\n')

def process(article_number, paper_id, paper, bibtex):
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
    authors = formatAuthors(paper['authors'])
    if 'author' not in fields:
        fields['author'] = authors
        print(paper_id, 'missing authors. Guess:', authors)
    fields['booktitle'] = '{Proceedings of the International Conference on New Interfaces for Musical Expression}'
    fields['address'] = ADDRESS
    fields['issn'] = '{2220-4806}'
    fields['year'] = '{%s}' % YEAR
    fields['month'] = MONTH
    fields['article-number'] = '{%d}' % article_number
    fields['abstract'] = '{%s}' % (paper['abstract'].replace('\u2028', '\n').replace('\u2029', '\n').replace('\n', ' '))
    if paper['video_yt']:
        fields['presentation-video'] = '{https://youtu.be/%s}' % paper['video_yt']
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
    paper['bibtex'] = bibtex

def dotize(x):
    parts = x.split(' ')
    last = parts[-1]
    first = ' '.join(parts[:-1])
    return f'{last}, {first}'
def formatAuthors(authors):
    return '{' + ' and '.join([dotize(x) for x in authors]) + '}'

main()
