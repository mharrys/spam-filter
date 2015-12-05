"""Machine learning utilities.
"""
import fs
import random

from extract import remove_email_headers, remove_html, remove_url
from sklearn import cross_validation
from sklearn.utils import shuffle

RANDOM = 3820178  # set to None for no specific seed
random.seed(RANDOM)


def read_split(spams, hams, spam_limit=None, ham_limit=None, test_size=0.1):
    """Return training and test dataset from specified spam and ham file
    paths.
    """
    names, targets = read_files(spams, hams, spam_limit, ham_limit)
    emails = read_data(names)
    return cross_validation.train_test_split(
        emails,
        targets,
        test_size=test_size,
        random_state=RANDOM,
    )


def read_one(spams, hams, spam_limit=None, ham_limit=None):
    """Return dataset from specified spam and ham file paths.
    """
    names, y = read_files(spams, hams, spam_limit, ham_limit)
    X = read_data(names)
    return X, y


def read_features(cls, paths, limit=None):
    """Return names and features for a class.
    """
    names = []
    for path in paths:
        names += fs.dir_walk(path)
    # shuffle paths
    names = shuffle(names, random_state=RANDOM).tolist()
    n = min(limit, len(names)) if limit is not None else len(names)
    targets = [cls] * n
    return names[:n], targets


def read_files(spams, hams, spam_limit=None, ham_limit=None):
    """Return filenames and targets for specified spam and ham directories
    recursively. Optional limit to maximum number of files.
    """
    spam_names, spam_targets = read_features(1, spams, spam_limit)
    ham_names, ham_targets = read_features(0, hams, ham_limit)
    # shuffle classes
    return shuffle(
        spam_names + ham_names,
        spam_targets + ham_targets,
        random_state=RANDOM,
    )


def count_class(cls, targets):
    """Return number of classes in targets.
    """
    return len([x for x in targets if x == cls])


def email_pre_process(email):
    """Return processed e-mail. It will remove e-mail headers, HTML tags and
    URLs.
    """
    email = remove_email_headers(email, subject=True)
    email = remove_html(email)
    email = remove_url(email)
    return email


def read_data(names):
    """Return processed e-mail content from specified filenames.
    """
    return [email_pre_process(fs.read_file(name)) for name in names]
