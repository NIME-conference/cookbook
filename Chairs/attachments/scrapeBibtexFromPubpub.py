'''
- Implement script `paperDatabaseInterface.py`.  
- Replace the check `.endswith('· NIME 2021'):` with your conference.  
- Run this script.  
- Go to script `writeBibtexToBibFile.py`.  
'''
import time
import pickle

from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from paperDatabaseInterface import getAllPapers

def main():
    driver = webdriver.Chrome('chromedriver')
    bibtex_dict = {}
    for paper in tqdm(getAllPapers()):
        bibtex = get(driver, paper.pub_url)
        bibtex_dict[paper.id] = bibtex
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
