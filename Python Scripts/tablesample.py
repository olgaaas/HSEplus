#! /usr/bin/python
# -*- coding: utf8 -*-

'''
Copyright © Alexey Khan 2012  All rights reserved
02.11.12; How to collect information into a file; 
'''

#Library::
from parsinglib import *
import datetime
import codecs
import sys, csv
from os.path import join, dirname

# Open the file
pfile = open('Example.csv', 'w')        # open('Example.csv', 'a')
head = 'Genre;'+'Similar;'+'Link\n'     # set a header for Excel-file
pfile.write(head)                       # write the header into the file

#Parsing::
print "Данный скрипт вытаскивает жанры, количество страниц, имя исполнителя, облако тегов и ссылку на страницу исполнителя с сайта last.fm \n"

body = get_body("http://www.last.fm/music")                                 # getting html body of the site
allGenres = find_where(body, '<li>All</li>', 'Popular Music on Last.fm')    # getting list of genres
allGenres = find_where(allGenres, '<li>', '</ul>')                          # deleting odd information
countGenres = spy_massiv(allGenres, '</li>')
    
for g in range(1):#countGenres                                                # for each genre::
    currGenre = find_where(allGenres, '<a href', '</li>')                   # getting the string with local genre
    currGenre = clear(currGenre, '')                                        # deleting add html tags
    allGenres = find_where(allGenres, '<li>', '')                           # changing the genres search-zone
    genreBody = get_body('http://www.last.fm/music/+tag/'+currGenre)        # getting html body of genre list
    numberOfPagesInGenre = find_where(genreBody, 'class="pagelink lastpage">', '</a>')                   # number of pages in this genre section
    numberOfPagesInGenre = re.sub(r'class="pagelink lastpage">','',numberOfPagesInGenre)                 # deleting odd html tags
    numberOfPagesInGenre = int(numberOfPagesInGenre)
    number = 1
    print 'genre:', currGenre
    print 'numberOfPagesInGenre:', numberOfPagesInGenre
    for p in range(3):#numberOfPagesInGenre
        genrePage = get_body('http://www.last.fm/music/+tag/'+currGenre+'?page='+str(number))
        performersList = find_where(genrePage, 'Popular in Russian Federation</a>', '<div class=\"pagination\">')   # getting list of performers
        performersList = find_where(performersList, 'clearit', '')
        countPerformers = spy_massiv(performersList, '<img height=\"126\"')
        performer = find_where(performersList, '<strong class=\"name\">','</strong>')                           # name of performer
        performer = clear(performer, '')
        similar = find_where(performersList, 'Similar to:', '</p>')                                             # similar to this performer
        similar = clear(similar, '')
        similar = re.sub(r'Similar to:','',similar)
        similar = re.sub(r'                                                                        ','',similar)
        similar = re.sub(r'                                ','',similar)
        similar = similar.split(', ')
        link2performer = find_where(performersList, '<a href=\"', '\"    class=\"name\">')
        link2performer = re.sub(r'<a href=\"','http://www.last.fm',link2performer)
        performerpage = get_body(link2performer)
        ptags = find_where(performerpage, '<section class=\"tags\">', '<ul>')
        ptags = find_where(ptags, 'content=\"','\">')
        ptags = re.sub(r'content=\"','',ptags)
        performerslist = find_where(performersList, 'clearit', '')
        number += 1
        print '\n\tperformer:', performer
        print '\tsimilar:', similar
        print '\tlink to performer:', link2performer 
        s = currGenre+';'+performer+';'+link2performer+'\n'
        pfile.write(s)    

 
pfile.close()  
print "done" 