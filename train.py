"""Train text classifier to detect spam/ham e-mail-messages.
"""
from ml import read_split, read_one, count_class

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.pipeline import Pipeline

CLASSES = ['ham', 'spam']
TARGETS = [0, 1]
COMBINE = True

SA_SPAM = ['data/spam-assassin/spam']
SA_HAM  = ['data/spam-assassin/easy_ham', 'data/spam-assassin/hard_ham']
ENRON_SPAM = ['data/enron/spam']
ENRON_HAM  = ['data/enron/ham']


print('Read features...')
if COMBINE:
    print('Training and test data from same corpus')
    SPAM = SA_SPAM + ENRON_SPAM
    HAM = SA_HAM + ENRON_HAM
    X_train, X_test, y_train, y_test = read_split(SPAM, HAM, 19300, 19300, 0.12)
else:
    print('Training and test data from separate corpus')
    X_train, y_train = read_one(ENRON_SPAM, ENRON_HAM, 17000, 17000)
    X_test, y_test = read_one(SA_SPAM, SA_HAM, 2300, 2300)


print('%s ham training emails' % count_class(0, y_train))
print('%s spam training emails' % count_class(1, y_train))
print('%s ham test emails' % count_class(0, y_test))
print('%s spam test emails' % count_class(1, y_test))


print('Create pipeline...')
clf = Pipeline([
    ('count', CountVectorizer(
        stop_words='english',
        ngram_range=(1, 2),
    )),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB()),
])


print('Training classifier on the training set...')
clf = clf.fit(X_train, y_train)


print('Evaluating classifier on the test set...')
print('Confusion matrix:')
y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)

cm_tn, cm_fn = cm[0][0], cm[0][1]
cm_tp, cm_fp = cm[1][1], cm[1][0]
print('%s spams correctly classified as spam' % cm_tp)
print('%s hams correctly classified as ham' % cm_tn)
print('%s hams incorrectly classified as spam' % cm_fp)
print('%s spams incorrectly classified as ham' % cm_fn)

print(classification_report(y_test, y_pred, target_names=CLASSES))
