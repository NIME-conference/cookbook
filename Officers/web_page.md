# Web page officer

Main task: Keep the nime.org domain running, and continue to develop the web page.

Action points:

1. Move web pages to a new platform (the current Wordpress install is too vulnreable)
2. Move the domain to new solution(s)
3. Consider further developments

Officers:

- Charles Martin
- Rodrigo Schramm


## Content on nime.org

The web page currently has these functions:

1. General information about the community and links to annual conferences.
2. Proceedings archive
3. (Partly) archive of annual conference web pages

There have been discussions about developing the community page further, for example with:

- A web forum, possibly connected to one or more mailing lists
- A news/blog section
- A directory of active NIME'rs and institutions

Considering recent social media developments, the two first may not be so relevant any longer. A directory could be useful, however, but needs maintenance if developed.

## Web platform

### Current solution

- Wordpress install on JustHost shared hosting provider
- Pros: already works
- Cons: looks a bit old, seems to be quite slow (from Australia anyway), hard to update if you're not Alexander or Jesse.
- we are currently using the papercite plugin to [generate the paper archive](https://nime.gitbook.io/conference-cookbok/officers/paper_proceedings#indexing-in-google-scholar), so it is critical to find another solution for this if we move away from wordpress.
- need to figure out where to archive old conference web pages (static pages with own formatting)


### Proposed Solution

- Jekyll website hosted on a static hosting provider (e.g., netlify).
- The static web content will all be composed in markdown
- The idea is that the markdown files are in a github repo and netlify is setup to pick them up on push and publish to their own host.
- Use `jekyll-scholar` plugin to generate proceedings archive page(s) from bibtex file.
- Allows a blog and is easy to update.


#### Dealing with the proceedings and website archive

- proceedings is too big to host on netlify (can't be stored directly in git repo).
- Probably the easiest option is to [host them in an AWS S3 static bucket](https://medium.com/@kyle.galbraith/how-to-host-a-website-on-s3-without-getting-lost-in-the-sea-e2b82aa6cd38) and redirect nime.org/proceedings [from Netlify](https://stackoverflow.com/questions/49283171/how-to-point-a-netlify-subdomain-to-an-aws-s3-bucket-via-cname). 
- This might work for the old NIME sites as well.
- Most nime sites are static, but one (2008) is in PHP --- can somebody convert this somehow??? (e.g., use [php2html](https://github.com/neurobin/php2html) Doesn't seem complicated but I don't want to have to host it somewhere with PHP installed.

#### Costs of Hosting

- Question 1: What's the current cost committed to hosting?
- Question 2: What are our needs going forward?

- Justhost suggests that our mean bandwidth is 110GB per month (min 80GB, max 130). At standard S3 rates this 2.3USD per month so probably nnot going to break the bank, and even if we become 10 times more popular it would be affordable.

- Netlify has a free tier (seems ok) and an expensive paid tier (45USD p/m). What does the paid tier get you?
- Might be fine to go with the free tier for the static page and pay for proceedings traffic directly on AWS. Not sure if that works, so will have to try.
