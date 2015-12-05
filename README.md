# Spam Filter

Simple spam filter trained with multinomial Naive Bayes.

## Corpus

[SpamAssassin](http://www.csmining.org/index.php/spam-assassin-datasets.html)
and [Enron-Spam](http://www.aueb.gr/users/ion/data/enron-spam/) was used when
developing this spam filter. Expecting directory structure with files of
e-mails in plain text. Every e-mail has any existing HTML-tags and URLs
removed and also its headers (except for the subject) before used.

## Results

When combining SpamAssassin and Enron-Spam into one corpus it appears to
perform almost too good in terms of precision and recall. However, the
performance drops when training on Enron-Spam and evaluating on SpamAssassin.

The Enron-Spam corpus is collected from 150 employees working at Enron and
SpamAssassin is a collection of donated e-mails. It could be that Enron-Spam
does not give enough variation for the spam filter to generalize.

The feature methods used for better results are only minor, the best
improvement comes from bi-grams.

## Potential problems and future works

There appear to be e-mails that are encrypted or with attachments that are
not removed but could potentially affect the results.

The feature vector dimensions are huge and most likely need to reduce their
dimensions for better results. It could also be interesting to use SVM over
Naive Bayes.

Lastly it would also be interesting to explore another corpus.

## Dependencies

[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) is used to
remove HTML-tags (used with [lxml](http://lxml.de)) and
[sklearn](http://scikit-learn.org/stable/index.html) is used for machine
learning specific tasks.

## Run

With the assumption that you have the datasets available as specified in
`train.py` and have set the desired random seed in `ml.py`.

    $ python train.py
