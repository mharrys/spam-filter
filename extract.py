"""Helper functions for removing unwanted metadata in text.
"""
import re

from bs4 import BeautifulSoup


def remove_email_headers(text, subject):
    """Remove email headers from specified text.
    """
    new_text = ''
    split_text = text.split('\n')
    i = 0
    n = len(split_text)
    while i < n:
        line = split_text[i]
        i += 1
        if line == '':
            break
        if subject and line.startswith('Subject:'):
            new_text += line[9:] + '\n'
    while i < n:
        line = split_text[i]
        i += 1
        new_text += line + '\n'
    return new_text


def remove_html(text):
    """Remove html-tags from specified text.
    """
    # there are some files that bs4 can't handle in one parse, must do it
    # twice
    bsoup = BeautifulSoup(
        BeautifulSoup(text, 'lxml').get_text(' '),
        'lxml'
    )
    return bsoup.get_text(' ')


def remove_url(text):
    """Remove URLs from specified text.
    """
    # this regex could improved for more types of URLs
    return re.sub(r'(?:\@|https?\://)\S+', ' ', text)
