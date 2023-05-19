# Procedure for Publishing the NIME Proceedings

The NIME website supports three types of proceedings: **papers**, **music** and **installations**, corresponding to the three review tracks that have traditionally taken place at NIME.

The yearly proceedings for NIME are defined by BibTeX files for each track that are published each year in the NIME bibliography repository: <https://github.com/NIME-conference/NIME-bibliography>

Publishing the yearly proceedings involves:

1. Collecting/collating/creating BibTeX files for each track
2. Collecting together correctly named PDF files
3. (If not using Pubpub) uploading PDF files to Zenodo for archiving and integrating DOIs into the BibTeX files
4. Depositing the BibTeX files in the [NIME Bibliography repository](https://github.com/NIME-conference/NIME-bibliography) (ask web or proceedings officers for help)
5. Deposit PDF files on the [NIME website](https://nime.org) (ask web officer for help).

**N.B.: The proceedings only includes submissions that have been both submitted and presented at NIME.**

## NIME Proceedings BibTeX Files

The canonical format for a NIME *paper* proceedings bibtex entry is:

```
@inproceedings{article_id,
  author = {},
  title = {},
  pages = {},
  booktitle = {Proceedings of the International Conference on New Interfaces for Musical Expression},
  editor = {}
  year = {},
  month = {}
  date = {},
  address = {},
  isbn = {},
  issn = {},
  articleno = {},
  track = {},
  doi = {},
  url = {http://www.nime.org/proceedings/year/article_id.pdf},
  urlsuppl1 = {},
  urlsuppl2 = {},
  urlsuppl3 = {},
  pdf = {},
  presentation-video = {},
  keywords = {},
  abstract = {}
}
```

## NIME Proceedings PDF Files

PDF files corresponding to proceedings entries should use `article_id` as their filename.

So, for example, a paper with `article_id` `martin2001a` should have a corresponding PDF file called `martin2001a.pdf`.

We don't have any particular standard for `article_id` and it may vary from year to year depending on the procedures used by individual NIME conference committees.

## Article and Page Numbers

It is useful to have both article numbers and page numbers for NIME submissions where possible. The reason is to help with citation in publications where "traditional" references to conference papers would always have some kind of page-like identifier.

- **article numbers**: This is basically pretty easy to implement, just number the accepted and presented papers.
- **page numbers**: It's reasonable to skip this for HTML publications, but if the main format is PDF this could be calculated with some maths using the the article number and number of length of each paper.

## Errors in BibTeX file

We consider the bibtex files to be living documents that are updated as and when errors are found. Nevertheless please consider some way to error-check proceedings submissions (e.g., transform the BibTeX to a big HTML document with Pandoc somehow and visually check for encoding errors).


