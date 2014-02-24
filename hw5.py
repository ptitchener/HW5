# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:36:25 2014

@author: paul
"""
import pickle
from pattern.web import *
import nltk, re, pprint
from urllib import urlopen
from bs4 import BeautifulSoup

def import_books():
    """
    oliver_twist_full_text = URL('http://www.gutenberg.org/ebooks/730.txt.utf-8').download()
    hard_times = URL('http://www.gutenberg.org/files/786/786-0.txt').download()
    our_mutual_friend = URL('http://www.gutenberg.org/cache/epub/883/pg883.txt').download()
    paperwick_papers = URL('http://www.gutenberg.org/cache/epub/580/pg580.txt').download()
    a = open('hard_times.txt','w')
    a.write(hard_times)
    a.close()
    b = open('oliver_twist.txt','w')
    b.write(oliver_twist_full_text)
    b.close()
    c = open('our_mutual_friend.txt','w')
    c.write(our_mutual_friend)
    c.close()
    d = open('paperwick_papers.txt','w')
    d.write(paperwick_papers)
    d.close()
    """
    url = "http://www.gutenberg.org/files/786/786-0.txt"
    oliver_twist= urlopen(url).read()
    a = open('oliver_twist1.txt','w')
    a.write(oliver_twist)
    a.close()
    
def read_book(book):
    a = open(book,'r')
    returns = a.read()
    a.close()
    return returns
    """
    a.close()
    a = open('oliver_twist.txt','r')
    oliver_twist = a.read()
    a.close()
    a = open('our_mutual_friend.txt','r')
    our_mutual_friend = a.read()
    a.close()
    a = open('paperwick_papers.txt','r')
    paperwick_papers.txt = a.read()
    a.close()
    """
def test(book):
    a = read_book(book)
    b = a.split()
    return b
    

"""
hard_times = URL('http://www.gutenberg.org/files/786/786-0.txt').download().decode('UTF-8')


tokens = nltk.word.tokenize(text)
"""
if __name__ == '__main__':
    #a =  read_book('hard_times.txt')
    print test('oliver_twist1.txt')