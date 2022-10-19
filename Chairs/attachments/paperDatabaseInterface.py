'''
Implement `getAllPapers()`.  
'''

from dataclasses import dataclass
from typing import Generator, List, Optional

@dataclass
class Paper:
    id: int
    authors: List[str]
    abstract: str
    pub_url: str
    video_url: str

    bibtex: Optional[str] = None

def getAllPapers() -> Generator[Paper]:
    # Implement this
    for i in ...:
        paper = ...
        yield paper
