#! /usr/bin/python
# -*- coding: utf-8 -*-

'''
Copyright © Alexey Khan 2012  All rights reserved
09.08.12
www.last.fm site parsing script, written to collect 
information about music in the OnjectsDB for
www.interestoria.com project.
'''

#Library::
import pymongo
from parsinglib import *
import datetime
import codecs
import sys
from os.path import join, dirname

#Connection to DataBase:
conn = pymongo.Connection()
db = conn['InterestoriaDB']
musicColl = db['music']

#Database checking

#musicColl.remove({})      
#for row in musicColl.find():          # print all collections
#    print row

#Parsing::
print "musicColl :: last.fm \n"
body = get_body("http://www.last.fm/music")                                 # getting html body of the site
genres = find_where(body, '<li>All</li>', 'Popular Music on Last.fm')       # getting list of genres
genres = find_where(genres, '<li>', '</ul>')                                # deleting odd information
countgenres = spy_massiv(genres, '</li>')    
for g in range(countgenres):                                                # for each genre::
    genre = find_where(genres, '<a href', '</li>')                          # getting the string with local genre
    genre = clear(genre, '')                                                # deleting add html tags
    genres = find_where(genres, '<li>', '')                                 # changing the genres search-zone
    genrebody = get_body('http://www.last.fm/music/+tag/'+genre)            # getting html body of genre list
    genre_n_pages = find_where(genrebody, 'class=\"lastpage\">', '</a>')    # number of pages in this genre section
    genre_n_pages = re.sub(r'class=\"lastpage\">','',genre_n_pages)         # deleting odd html tags
    n_pages = int(genre_n_pages)
    number = 1        
    #print 'genre:',genre                                                    # number of the current page in genres section
    for p in range(n_pages):
        genrepage = get_body('http://www.last.fm/music/+tag/'+genre+'?page='+str(number))
        performerslist = find_where(genrepage, 'Popular in Russian Federation</a>', '<div class=\"pagination\">')   # getting list of performers
        performerslist = find_where(performerslist, 'clearit', '')
        countperformers = spy_massiv(performerslist, '<img height=\"126\"')                                         # number of performers on the current page
        for j in range(countperformers):
            performer = find_where(performerslist, '<strong class=\"name\">','</strong>')                           # name of performer
            performer = clear(performer, '')
            similar = find_where(performerslist, 'Similar to:', '</p>')                                             # similar to this performer
            similar = clear(similar, '')
            similar = re.sub(r'Similar to:','',similar)
            similar = re.sub(r'                                                                        ','',similar)
            similar = re.sub(r'                                ','',similar)
            similar = similar.split(', ')
            link2performer = find_where(performerslist, '<a href=\"', '\"    class=\"name\">')
            link2performer = re.sub(r'<a href=\"','http://www.last.fm',link2performer)
            performerpage = get_body(link2performer)
            ptags = find_where(performerpage, '<section class=\"tags\">', '<ul>')
            ptags = find_where(ptags, 'content=\"','\">')
            ptags = re.sub(r'content=\"','',ptags)
            print 'performer:', performer
            tracklist1 = get_body(link2performer+'/+tracks')
            ntrackspages = find_where(tracklist1, 'class=\"lastpage\">', '</a>')     # number of pages with performer's tracks
            ntrackspages = re.sub(r'class=\"lastpage\">','',ntrackspages)
            ntrackspages = int(ntrackspages)
            page = 1
            for t in range(ntrackspages):
                print 'page #'+str(page)
                tracklistbody = get_body(link2performer+'/+tracks?page='+str(page))
                tracklist = find_where(tracklistbody, '<td class=\"positionCell\">', '')
                ntracksonpage = spy_massiv(tracklistbody, '<td class=\"positionCell\">')
                print 'tracks on page:', ntracksonpage
                for s in range(ntracksonpage): # run through all string on the tracklistpage
                    trackfield = find_where(tracklist, 'class=\"positionCell\">', '<td class=\"lovedCell\">')
                    track = find_where(trackfield, '<a href=\"', '</a>')
                    tracklink = find_where(track, 'href=\"','"   >')
                    tracklink = re.sub(r'href=\"','',tracklink)
                    tracklink = 'http://www.last.fm'+tracklink
                    track = clear(track, '')
                    if (musicColl.find({'name': track, 'owner': performer}).count() > 0):
                        tracklist = find_where(tracklist, '<td class=\"positionCell\">', '')
                        #print 'track \"', track ,'\" already in db'
                        continue
                    else:
                        tracklist = find_where(tracklist, '<td class=\"positionCell\">', '')
                        try:
                            trackpage = get_body(tracklink)
                            trtags = find_where(trackpage, '<section class=\"tags\">', '<ul>')
                            trtags = find_where(trtags, 'content=\"','\">')
                            trtags = re.sub(r'content=\"','',trtags)
                            if genre not in trtags:
                                trtags += ', '+genre
                            if '_' in trtags:
                                trtags = ptags
                            trtags = trtags.split(', ')
                            trobject = {
                                        'name': track,
                                        'owner': performer,
                                        'tags': trtags,
                                        'similar': similar
                                       }
                            musicColl.insert(trobject)
                            #print trobject
                            #print tracklink
                        except:
                            continue
                page += 1 
            performerslist = find_where(performerslist, 'clearit', '')
            
            #print tags, link2performer, performer, similar 
        number += 1

print 'musicColl created'        