'''
replace `filename = 'withChannels.pickle'` with whatever input data.  
`papers` is a list of dict. A dict should have `paper_id`, and `pub` is URL to the pubpub Pub.  
Replace the check `.endswith('· NIME 2021'):` with your conference.  
'''
import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from jdt import jdtIter

def main():
    filename = 'withChannels.pickle'
    print('Reading from', filename)
    with open(filename, 'rb') as f:
        papers = pickle.load(f)
    driver = webdriver.Chrome('chromedriver')
    bibtex_dict = {}
    for paper in jdtIter(papers):
        paper_id = paper['paper_id']
        bibtex = get(driver, paper['pub'])
        bibtex_dict[paper_id] = bibtex
    with open('bibtex_dict.pickle', 'wb') as f:
        pickle.dump(bibtex_dict, f)
    driver.close()

def get(driver : WebDriver, url):
    driver.get(url)
    if not driver.title.strip().endswith('· NIME 2021'):
        print('Error. title is:', driver.title)
        from console import console
        console({**globals(), **locals()})

    driver.execute_script('''
        document.getElementsByClassName(
            'more-cite-options-button'
        )[0].click();
    ''')

    cites = driver.find_elements_by_class_name('csl-entry')
    def findBib():
        for cite in cites:
            if '@inproceedings' in cite.text:
                return cite.text
        return False

    while not findBib():
        time.sleep(1)
    return findBib()

main()
