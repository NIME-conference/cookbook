# Paper Chair


## Before the conference


### Prepare Call for participation (September)

The CFP is usually adjusted slightly from year to year, but not be drastically different. Please refer to [previous calls](../calls/cfp2012.md).


### Set up the Conference Management System (November)

NIME used Easyconf as the Conference Management System (CMS) for many years. After some bad experiences with server crashes, lack of support, and lack of multi-track functionality, we decided to move away. From 2012 NIME has been using Precision Conference as CMS. Chairs have reported this to be a solid system, although with some of a learning curve. It is also quite costly.

In 2019 the SC has decided to switch to a different system. The discussion revealed that there are two main options:

- EasyConf
- Microsoft Conference Management Toolkit

The former is used by SMC, MOCO (and many others). The latter is used by ISMIR, WAC (and many others). I don't have a strong opinion on which one to use. For the SC the most important is not to change every year. So if we decide on something we should stay with it for a few years.

### Recruit reviewers (December)

* When it comes to reviewers, you can get lists from previous chairs (or it may be in the system). It is common to add some local people each year, and some of these should probably be removed if they are not regular NIMErs.

* Be careful about accepting to take on reviewers that start out saying they have little time, and can do the reviews a bit late. If people first start being late, they may be vary late, or not deliver at all. It is a very tight

* Be very strict about deadlines, and plan well ahead. The reviewer pool should be ready way before the deadline, preferably before Christmas. It is better to get too many than too few.

* Prepare reviewers and meta-reviewers about what is coming when. So a week before they should get to action, you can send them an e-mail and inform them about when they will receive their assignments.


### Peer review (February)

* The paper chair(s) assign papers to reviewers (3-4 per paper to get enough) and follow up the deadlines
* A group of meta-reviewers write the summaries and suggest acceptance
* The paper chair(s) do the final selection

In the interest of running the process as smoothly as possible, the paper chair(s) should do the review assignment and follow-up. This is how it has always been (we only started with meta-reviewers in 2014). The CMS helps out a lot by coming up with suggestions of reviewers based on expertise. Having a centralized reviewer assignment also helps in avoiding individuals to be contacted by multiple meta-reviewers.


## Confirmation letter to send ##

After paper reviewing there are different kinds of letter to send:
* submitted and accepted as paper
* submitted as paper but downgraded to poster
* submitted as poster and accepted as such
* submitted as concert but performed as club
* submitted as concert but downgraded to demo

#### Double-blindedness

This is how double-blind policy is implemented in the PCS System used at NIME:

1. authors do not know external reviewer nor meta-reviewer names   
2. external reviewers do not know author names   
3. meta-reviewers know both author and external reviewer names  
4.  external reviewers do not know other external reviewer names   
5. external reviewers know meta-reviewer names

The only strictly double-blind part is that between external reviewers and authors.



## During the conference

### Presentation duration

Previously there was a difference in presentation time between short and long papers. That has changed, and all presentations are now equally long.

There have been different duration of the talks, but they generally follow this pattern:

* 10-15 min presentation + 3 min questions + 2 min turnover

Remember to inform presenters about the duration of talks every time you have the chance, since people tend to forget.


### Running paper sessions

Time is short, so it is important to have a structured approach to chairing the oral sessions.
The paper chair needs to find session chairs to run each session. It is common to use experienced participants as session chairs, but please also consider giving new people a chance (and remember the diversity also of session chairs).

It is important that the paper chair clearly informs the session chairs about their duties:

- Arrive early to the session, and welcome all presenters.
- Ask presenters to test their setup before their session.
- Start on time, every minute matters. Remember to close the doors.
- Keep track of the time, and signal to presenters when there are 5, 2, 0 minutes left.
- Ask next presenters to set up during the Q&A session.

Please also ensure that you have volunteers available to assist during the session. Ideally you will have one volunteer helping with the audiovisual setup, and at least one volunteer to run with microphones during Q&A sessions.

Remember that session chairs do a very important job during the conference! An important part of the job is to smile, breath, and help nervous presenters to relax. But it is equally important to keep the time, nobody likes to be delayed to a coffee break.


### No-shows

NIME do not accept remote presentation, video presentation or presentations by non-authors.

The reason for this is that the conference should not only be a place for publishing papers (then a journal is more appropriate), but be a meeting point of people. That is not possible if the authors are not present.

No-shows happen, for various reasons, but it should really be discouraged. The most efficient way of doing this, is to remove no-show papers from the proceedings.


## After the conference


### Getting the proceedings on NIME.org

The nime.org archive is built on [BibTeX files](https://github.com/NIME-conference/NIME-bibliography) stored at Github. As paper chair it is your job to prepare a complete BibTeX file adhering to the NIME standards. The steps involved in this is as follows.

#### Remove papers that were not presented

There are always some accepted papers that are not presented for various reasons. No matter the reason, papers that are not presented at the conference should be removed from the proceedings. This is because the proceedings should reflect what actually happened at the conference. It is also very important to let all (future) authors know that NIME has a strict no-show procedure.

#### Fix errors in the metadata or papers

Due to the short time in preparing the proceedings before the conference, there may be occasional errors in metadata (author names, affiliations, etc.) or in the PDF files (most often wrong page layout, missing fonts, low-resolution images, etc.).

It is in NIME's interest to have as good metadata and PDFs as possible, so we do accept such error corrections and minor PDF modifications.

#### Export from PrecisionConf

When the basic "post-processing" of the proceedings is done, it is time to generate the BibTeX file. As of 2018 it should be possible to export BibTeX directly from Precision Conference. Prior to that we had to do some post-processing with the script [Precision2BibTeX](https://github.com/NIME-conference/Precision2BibTeX).


#### Massaging the BibTeX file

The exported BibTeX file need some "massaging" to match the other BibTeX files in the repository. Please check the [files on Github](https://github.com/NIME-conference/NIME-bibliography/tree/master/BibTeX) to see how the file shold be formatted. Typically this includes:

- Check the title of the proceedings. It should be the generic title "Proceedings of the international conference on new interfaces for musical expression". The year and place should be included in separate fields, not as part of the title. This is because the ISSN for the series is bound to the generic proceedings title.
- Check that abstracts are included for all papers. Please also check that there a no line-breaks in the abstract.
- Check weird formatting (typically unicode-related issues).
- Insert right link to PDFs. Should be something like nime20XX_ID.pdf.

#### Send the material to the paper proceedings officer

The NIME paper proceedings officer will help with the above, and will also do the final upload to nime.org.

### Upload to Zenodo

NIME has decided to use Zenodo for archival of papers.


### Indexing

Indexing of the proceedings is important for the visibility of the papers. We will work more on improving this in the future.

#### Indexing in Google Scholar

The [papercite](https://wordpress.org/plugins/papercite/) plugin used on nime.org contains metadata information that is indexed by Google Scholar. So nothing else should be needed than getting the papers on nime.org.

#### Indexing in DBLP

For several years NIME was indeded in [DBLP](http://www.informatik.uni-trier.de/~ley/db/conf/nime/index.html). However, after they changed their submission format, we never managed to back on track.

Here is [info](https://dblp.uni-trier.de/faq/How+can+I+submit+meta+data+for+a+complete+journal+or+conference.html) on how to submit to DBLP.

#### Indexing in ACM

The same is true for ACM, with which we have not been able to index for several years either. This is important to work on, hence the need for someone to work on this in particular.

#### Scopus

A request to register NIME in Scopus was sent in June 2018. They have a long processing time, and we should expect a reply in 2019.  
