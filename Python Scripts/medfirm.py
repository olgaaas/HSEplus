#! /usr/bin/python
# -*- coding: cp1251 -*-
import datetime
import codecs
import csv

'''
Copyright © Alexey Khan 2012  All rights reserved
27.08.12
www.medfirm.ru site parsing script, written to collect 
information about hospitals and pharmacy in Russia.
'''

#Library
import httplib, sys, re
import locale, urllib, urllib2
import random
from parsinglib import *
          
#WORK

#file = open("medfim.csv", "w")           
body = get_body('http://medfirm.ru/')
body = find_where(body,'<!--������� ������-->','</table>')

# only big cities (before regions)
cities = find_where(body,'<p><strong>������� ������ ������</strong></p>','<!--�������-->')
count_cities = spy_massiv(cities,"<a class")                           # searching in array
for i in xrange(count_cities):
    url_cities = find_where(cities,'href=\"','\">')                    # searching links  
    city_name = find_where(cities,'<a','</a>')                         # delete all tags
    city_name = clear(city_name,'')                                    # names of cities
    cities = find_where(cities,'href=\"','')                           # clear useless information  
    url_cities = re.sub(r'href=\"','http://medfirm.ru',url_cities)     # building links
    url_cities = re.sub(r'\.html','',url_cities)
        
    # find the number of pages
    body2 = get_body(url_cities+'-1.html')                                                  
    n_pages = find_where(body2, '��������:','</a> </div>')
    n_pages = clear(n_pages, '')
    n_pages = find_where(n_pages, '...','') 
    n_pages = re.sub(r"&[^;]*;","",n_pages)
    n_pages = re.sub(r"\.\.\.","",n_pages)
    
     
    for j in xrange(int(n_pages)):                                # looking through all pages for links to each med. center                   
        body3 = get_body(url_cities+'-'+str(j)+'.html') 
        med_links = find_where(body3, '<table class="dealer" border="0" summary="">', '<td colspan="2" style="text-transform: uppercase;">')
        count_med = spy_massiv(med_links,"href")                  # number of links to med. centers
        print '��������', str(j)
        print '����� ������ �� ��������:', str(count_med)
        for q in xrange(count_med): 
            print '������ �� ����� �� ����:', str(q)
            if (j == 167) and (q == 6):                                                # on page 168 line 7 there is a broken link
                med_links = find_where(med_links, 'href=\"', '')                       # new link
                continue             
            url_med = find_where(med_links, 'href=\"', '\">')
            url_med = re.sub(r'href=\"', 'http://medfirm.ru', url_med)
            body_main = get_body(url_med)                                               # main information about med. center  
            name = find_where(body_main, '<title>', '</title>')
            name = re.sub(r'<title>','',name)  
            name = name.strip()                                                         # name of organization
            address = find_where(body_main, '<b>�����:</b>', '<br><b>�������:')  
            address = re.sub(r'<b>�����:</b>', '', address)  
            address = address.strip()                                                   # address of organization
            phone = find_where(body_main, '<br><b>�������:', '<b>��� ������������:') 
            phone = clear(phone, '')
            phone = re.sub(r'�������:', '', phone)
            phone = phone.strip()                                                       # phone of organization
            worktype = find_where(body_main, '<b>��� ������������:', '<noindex>') 
            worktype = re.sub(r'<b>��� ������������:','',worktype)
            worktype = clear(worktype,'')
            worktype = worktype.strip()
            med_links = find_where(med_links, 'href=\"', '')                            # new link
            #s = name+';'+address+';'+phone+';'+worktype+'\n'
            #file.write(s)
            print name
            print address
            print phone
            print worktype

# only regions
regions = find_where(body,'<!--�������-->','')
count_regions = spy_massiv(regions,"<a class")                 # searching in array
for r in xrange(count_regions):  
    if r == 5 or r == 62 or r == 80:                                      # regions n. 6, n. 62 and n. 81 have no med. centeres 
        regions = find_where(regions,'href=\"/med','')
        continue    
    url_reg = find_where(regions,'href=\"/med','\">')              # searching links  
    url_reg = re.sub(r'href=\"','http://medfirm.ru',url_reg)       # building links
    regions = find_where(regions,'href=\"/med','')   
    body_reg = get_body(url_reg) 
    body_reg = find_where(body_reg, '<a class=\"tx\" href', '</tr></table>')
    count_m = spy_massiv(body_reg, "a class")
    for k in xrange(count_m): 
        link = find_where(body_reg,'href=\"','\">')
        link = re.sub(r'href=\"', 'http://medfirm.ru', link)
        body_reg = find_where(body_reg, 'border=\"0\">', '')
        npages_body_m = get_body(link)
        npages_body_m = find_where(npages_body_m, '��������', '</div>')
        npages_body_m = clear(npages_body_m, '')        
        if '...' in npages_body_m:
            npages_body_m = find_where(npages_body_m, '...','')
            npages_body_m = re.sub(r"&[^;]*;","",npages_body_m)
            npages_body_m = re.sub(r"\.\.\.","",npages_body_m)
        else:
            npages_body_m = re.sub(r"&[^;]*;","",npages_body_m)
            npages_body_m = re.sub(r'��������:','',npages_body_m)       
    
        hospitals = find_where(get_body(link), '<!-- ����� ������ ����������-->', '<tr><td colspan="2" style="text-transform: uppercase;">')   
        count_hospitals = spy_massiv(hospitals, '<a class')                 # how many hospitals on a page
        for l in xrange(count_hospitals): 
            link_hosp = find_where(hospitals,'href=\"','\">')               # links to hospitals
            link_hosp = re.sub(r'href=\"',' http://medfirm.ru',link_hosp)
            body_hosp = get_body(link_hosp)             
            name_h = find_where(body_hosp, '<h1>', '</h1>')
            name_h = re.sub(r'<h1>','',name_h)  
            name_h = name_h.strip()                                                 # name of organization
            address_h = find_where(body_hosp, '<b>�����:</b>', '<br><b>�������:')  
            address_h = re.sub(r'<b>�����:</b>', '', address_h)  
            address_h = address_h.strip()                                           # address of organization
            phone_h = find_where(body_hosp, '<br><b>�������:', '<b>��� ������������:') 
            phone_h = clear(phone_h, '')
            phone_h = re.sub(r'�������:', '', phone_h)
            phone_h = phone_h.strip()                                               # phone of organization
            worktype_h = find_where(body_hosp, '<b>��� ������������:', '') 
            worktype_h = re.sub(r'<b>��� ������������:','',worktype_h)
            worktype_h = find_where(worktype_h, ' ', '<noindex>')
            worktype_h = worktype_h.strip()
            hospitals = find_where(hospitals,'href=\"','')                          # new link
            s = name_h+';'+address_h+';'+phone_h+';'+worktype_h+'\n'
            #file.write(s)
            #print s
            print name_h
            print address_h
            print phone_h
            print worktype_h
              
#file.close()     
        
        
        