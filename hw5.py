# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:36:25 2014

@author: paul
"""
import pickle
from pattern.web import *
from urllib import urlopen
import collections
#import numpy

#import matplotlib as mpl

def import_books():
    
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

def strip_extra(book):
    a = read_book(book)

    try:
        end = a.index('End of the Project Gutenberg')
    except ValueError:
        try:
            end = a.index('*** END OF')
        except ValueError:
            end = a.index('***END OF')
    
    ind1 = a.index('***')
    start= a.index('***',ind1)
    return a[start:end] 
        
def delete_extra(book):
    b = strip_extra(book)
    b.lower
    a = b.split()
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
        elif '\xef\xbb\xbf' in a[i]:
            a[i] = a[i].translate(None,'\xef\xbb\xbf')
    return a
            

def makesdic(book):
    """
    Take a list of strings. Figure out how many times a specific word occurs. 
    And then make that into a dictionary.
    """
    
    #text = "hello there hi there"
    text= delete_extra(book)
    #text = ''.join(str(e) for e in text_list)
    dic = dict()
    dic = {'_all_':0}
    dic_100 = {}
    return collections.Counter(text)
    #for w in text:
        #dic['_all_'] +=1
        #if w in dic.keys():
            #dic[w] = dic[w]+1
            #if dic[w] >100:
                #dic_100[w] = dic[w]
            
        #else:
            #dic[w] = 1
   # return dic_100
    

    
def word_freq(book):
    count = makesdic(book)
    a = sum(count.values())
    for w in count:
        #f w != '_all_':  
        count[w] = float(count[w])/(a)
    return count
    
    
def list_sort(book):
    #a = word_freq(book)
    a = {'the':5,'said':40,'blah':1,'super':553}
    b = [(v, k) for v,k in a.iteritems()]
    #sort = sorted(b, key=lambda tup: tup[0])
    return sort
    
def compare(book1,book2):
    freq1 = word_freq(book1)
    freq2 = word_freq(book2)
    
    #freq1 = {'red':5,'blue':24,'green':2}
    #freq2 = {'red':2,'green':5,'purple':4}
    c = dict(freq1.items() + freq2.items())
    all_words = map(list,zip(c))
    #freq1_list = recursive_flatten(map(list,zip(freq1)))
    #freq2_list = recursive_flatten(map(list,zip(freq2)))
    freq1_list = freq1.values()
    freq2_list = freq2.values()
    #print freq2_list
    #return c
    flattened = recursive_flatten(all_words)
    L1 = []
    L2 = []
    for w in flattened:
        L1.append(freq1.get(w, 0))
        L2.append(freq2.get(w, 0))
        
    #print L1
    #print L2
    mag1 = magnitude(freq1_list)
    mag2 = magnitude(freq2_list)
    dot = dotprod(L1,L2)
    
    similarity = dot/(mag1*mag2)
    return similarity
    
    
    
    
    
    
def magnitude(L):
    if type(L) != list:
        raise Exception("L must be a list")
    a = 0
    
    for w in L:
        a = a + w**2
    return a**.5

def dotprod(L1,L2):
    if len(L1) != len(L2):
        raise Exception('Lenghts of vectors must be equal')
    i = 0
    a = 0
    for i in range(len(L1)):
        a = a + L1[i]*L2[i]
    return a
                 
        
        

def recursive_flatten(L):
    L1 = []
    for i in range(len(L)):
        if type(L[i])==list:
            L1  = L1 + (recursive_flatten(L[i]))
        else:
           L1.append(L[i])
    return L1
  

def make_plot(Z):
    if type(A) != list:
        raise Exception("TypeError: make_plot input must be a list")
        
    #make x and y arrays
    i = 0
    for i in range(len(A)):
        B = A[i]
        
        for j in range(len(B)):
            Y_int[j] = j
            X_int[j] = i
        X.append(X_int)
        Y.append(Y_int)
    
    #finding minimums and maximums of the z array
    z_min, z_max = np.abs(Z).min(), np.abs(Z).max()

    mpl.pyplot.pcolor(X,Y,Z,vmin=z_min, vmax=z_max)
        
    mpl.colorbar()

def compare_all():
    l1 = ['Plato.txt','Dar_voy.txt','PP_Aust.txt','hard_times.txt']
    output1 = []
    compare_once = {}
    for w in l1:
        l_int = []
        for x in l1:
            if w ==x:
                compare_int =1.0

            else:
                try:
                    compare_int = compare_once[x,w]
                except:
                    compare(w,x)
                    compare_int = compare(w,x)
                    compare_once[w,x] = compare_int

            l_int.append(compare_int)  
            print compare_int
            

        output1.append(l_int)
    return output1


if __name__ == '__main__':
    #a =  read_book('hard_times.txt')

    #print test('oliver_twist1.txt')
    #print makesdic('oliver_twist.txt')
    #print word_freq('oliver_twist.txt')
    #a = word_freq

    #print list_sort('blah')
    print compare_all()
    #print word_freq('hard_times.txt')
    #print strip_extra('Dar_voy.txt')
    #z = [[1,2,3],[4,5,6],[7,8,9]]
    #make_plot(z)
    #mpl.savefig('color.png')