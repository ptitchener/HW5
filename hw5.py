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
def split_book(book):
    a = read_book(book)
    b = a.split()
        
def delete_extra(book):
    #a = ['asdf','asdf','adsf','\xe2\x80\x94asdf','asdf']
    #b = read_book(book)
    #a = b.split()
    a = ['\xe2\x80\x98My', 'dear', 'Bounderby,\xe2\x80\x99', 'Mr.', 'Gradgrind', 'began', 'in', 'reply.', '\xe2\x80\x98Now,', 'you\xe2\x80\x99ll', 'excuse', 'me,\xe2\x80\x99', 'said', 'Bounderby,', '\xe2\x80\x98but', 'I', 'don\xe2\x80\x99t', 'want', 'to', 'be', 'too', 'dear.', 'That,', 'to', 'start', 'with.', 'When', 'I']
    i = 0
    for i in range(len(a)):
        if '\xe2\x80\x94' in a[i]:
            a[i] = a[i].translate(None,'\xe2\x80\x94')
        elif '\xe2\x80\x99' in a[i]:
            a[i] = a[i].translate(None,'\xe2\x80\x99')
        elif '\xe2\x80\x98' in a[i]:
            a[i] = a[i].translate(None,'\xe2\x80\x98')
        elif '.' in a[i]:
            a[i] = a[i].translate(None,'.')
    return a
            

"""
hard_times = URL('http://www.gutenberg.org/files/786/786-0.txt').download().decode('UTF-8')


tokens = nltk.word.tokenize(text)
"""
if __name__ == '__main__':
    #a =  read_book('hard_times.txt')

    print test('oliver_twist1.txt')
    



"""
Take a list of strings. Figure out how many times a specific word occurs. 
And then make that into a dictionary.
"""

def makesdic():
    text = "hello there hi there"
    dic = dict()
    for w in text.split():
        if w in dic.keys():
            dic[w] = dic[w]+1
        else:
            dic[w] = 1
    return dic





