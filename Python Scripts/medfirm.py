#! /usr/bin/python
# -*- coding: cp1251 -*-
import datetime
import codecs
import csv

'''
Created on 19.01.2011

@author: Mih
'''

#Library
import httplib, sys, re
import locale, urllib, urllib2
import random


locale.setlocale(locale.LC_ALL, '')

#Function Get body
def get_body(url):
    html = urllib.urlopen(url)
    html = html.read()
    return html

def get_getmethod_body (el_1,el_2,el_3=None):
    
    el_1 = re.sub(r"http://", "", el_1)
        
    conn = httplib.HTTPConnection(el_1)
    conn.request("GET", el_2)
    resp = conn.getresponse()
    
    if resp.status != 200:
        data = "Can't connect to "+el_3
        sys.exit()
        return data
   
    data = resp.read()    
    conn.close()
    
    return data
    
#find where
def find_where(html,b_search,e_search):
   
    data = html
    if data.find(b_search) != -1:
        data = data[data.find(b_search,1):]
    
        if e_search != "":
            data = data[:data.find(e_search)]

    return data

#hook
def hook (html,find_element):
    
    data = html
    
    if data.find(find_element) == -1:
        data = "not find"
        return data
    else:
        data = "find"
        return data
        
        
#clear
def clear(perem,change = None):
    if change == None:
        perem = re.sub(r"<[^>]*>","",perem)
        
    else:
        perem = re.sub(r"<[^>]*>",change,perem)
    perem = re.sub(r"\n",change,perem)
    perem = re.sub(r"\r",change,perem)
    perem = re.sub(r"\t",change,perem)
    
    
    return perem        
#get link
def get_link(html,el_1,pice_link,el_2):
    
    data = html
    if el_1 != "":
        data = data[data.find(el_1,1):]
    if pice_link != "":
        data = data[data.find(pice_link,1):]
    
    test = re.sub(r"<", "x87", data)
    
    if test=="x87":
        curURL = ""
        return curURL
    if test != "x87":
        if data.find(el_2) != -1:
            index = data.index(el_2,0,5000)
            curURL = data [0:index]
            
            curURL = re.sub(r"\n", "", curURL)
            curURL = re.sub(r"\r", "", curURL)
            curURL = re.sub(r"\t", "", curURL)
            
            return curURL
        else:         
            curURL = "no result"
            return curURL

#get field
def get_field(html,el_1,el_2):
    
    data = html
    data = data[data.find(el_1,0):]
    
    test = re.sub(r">", "x87", data)
    if test=="x87":
        field = ""
        return field
    if test != "x87":
        if data.find(el_2) != -1:
            index = data.index(el_2,0,20000)
            field = data [0:index]
                
            field = re.sub(r"\n", "", field)
            field = re.sub(r"\r", "", field)
            field = re.sub(r"\t", "", field)
    
            return field
        
        else:   
                  
            field = "no result"
            return field

#return count in massiv    
def spy_massiv (p_body,element):
     
    count = 0
       
    while hook(p_body,element) == "find":

        b_search = element
        e_search = ""

        p_body = find_where(p_body,b_search,e_search)
        
        count = count + 1
        
    return count-1
        
#get body use proxies
def get_b_proxy(url=None):
    
    status = "bad"
        
    mas = ['127.0.0.1:8118']
    
    headers = {"User-Agent" : "Opera/9.64 (Windows NT 5.1; U; en) Presto/2.1.1",
           "Accept" : "text/html, application/xml;q=0.9, application/xhtml+xml, image/ png, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1",
           "Accept-Language" : "ru,uk-UA;q=0.9,uk;q=0.8,en;q=0.7",
           "Accept-Charset" : "iso-8859-1, utf-8, utf-16, cp-1251, *;q=0.1",
           "Accept-Encoding" : "identity, *;q=0",
           "Connection" : "Keep-Alive"}
    
    
    while status is "bad":
        
        buf = random.sample(mas,1)
        
        proxy = buf[0]
        
        print "Use proxy, current proxy: "+proxy     

        proxy_handler = urllib2.ProxyHandler( {"http" : proxy} )
        
        opener = urllib2.build_opener(proxy_handler)
        
        urllib2.install_opener(opener)

        if url is None:
            
            url = "http://www.2ip.ru"
    
            page_request = urllib2.Request(url, headers = headers)
    
            try:
                data = urllib2.urlopen(page_request).read()
            except (IOError), msg:
                print msg
                status = "bad"
            else:
                                
                el_1 = "<big>"
                el_2 = "</big>"
                
                ip = get_field(data,el_1,el_2)
                ip = re.sub(r"</span>", "", ip)
                ip = re.sub(r"<big>", "", ip) 
                
                el_1 = "??? ???????:"
                el_2 = "</td>"
                
                b = get_field(data,el_1,el_2)
                b = re.sub(r"</th><td><img  alt=\"\" src=\"/img/Firefox.png\"/>", " ", b)
                
                el_1 = "<img alt=\""
                el_2 = "\" src=\""
                
                country = get_field(data,el_1,el_2)
                country = re.sub(r"<img alt=\"", "??????: ", country)
                
                print b
                print "Ваш IP адрес:"+ip
                print country

                status = "ok"
            
        if url is not None:
                
            page_request = urllib2.Request(url, headers = headers)
                
            try:
                data = urllib2.urlopen(page_request).read()               
            except(IOError), msg: 
                
                errors = {"404":"Ошибка: нет такой страницыы",
                          "400":"Ошибка: синтаксическая",
                          "500":"Ошибка: Ошибка сокета",
                          "504":"Ошибка: Ошибка сервера или скорее всего ошибка в адресе"}
                
                #print msg
                
                cur_error = get_field(str(msg),"Error ",":")
                cur_error = re.sub(r"Error ","",cur_error)
                
                print errors[cur_error]
                
                status = "ok"
                
            else:
                
                status = "ok"
                return data
                      
#WORK

#file = open("medfim.csv", "w")           
body = get_body('http://medfirm.ru/')
body = find_where(body,'<!--Крупные города-->','</table>')

# only big cities (before regions)
cities = find_where(body,'<p><strong>Крупные города России</strong></p>','<!--Регионы-->')
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
    n_pages = find_where(body2, 'Страницы:','</a> </div>')
    n_pages = clear(n_pages, '')
    n_pages = find_where(n_pages, '...','') 
    n_pages = re.sub(r"&[^;]*;","",n_pages)
    n_pages = re.sub(r"\.\.\.","",n_pages)
    
     
    for j in xrange(int(n_pages)):                                # looking through all pages for links to each med. center                   
        body3 = get_body(url_cities+'-'+str(j)+'.html') 
        med_links = find_where(body3, '<table class="dealer" border="0" summary="">', '<td colspan="2" style="text-transform: uppercase;">')
        count_med = spy_massiv(med_links,"href")                  # number of links to med. centers
        print 'Страница', str(j)
        print 'Число ссылок на странице:', str(count_med)
        for q in xrange(count_med): 
            print 'Ссылка по счету от нуля:', str(q)
            if (j == 167) and (q == 6):                                                # on page 168 line 7 there is a broken link
                med_links = find_where(med_links, 'href=\"', '')                       # new link
                continue             
            url_med = find_where(med_links, 'href=\"', '\">')
            url_med = re.sub(r'href=\"', 'http://medfirm.ru', url_med)
            body_main = get_body(url_med)                                               # main information about med. center  
            name = find_where(body_main, '<title>', '</title>')
            name = re.sub(r'<title>','',name)  
            name = name.strip()                                                         # name of organization
            address = find_where(body_main, '<b>Адрес:</b>', '<br><b>Телефон:')  
            address = re.sub(r'<b>Адрес:</b>', '', address)  
            address = address.strip()                                                   # address of organization
            phone = find_where(body_main, '<br><b>Телефон:', '<b>Вид деятельности:') 
            phone = clear(phone, '')
            phone = re.sub(r'Телефон:', '', phone)
            phone = phone.strip()                                                       # phone of organization
            worktype = find_where(body_main, '<b>Вид деятельности:', '<noindex>') 
            worktype = re.sub(r'<b>Вид деятельности:','',worktype)
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
regions = find_where(body,'<!--Регионы-->','')
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
        npages_body_m = find_where(npages_body_m, 'Страницы', '</div>')
        npages_body_m = clear(npages_body_m, '')        
        if '...' in npages_body_m:
            npages_body_m = find_where(npages_body_m, '...','')
            npages_body_m = re.sub(r"&[^;]*;","",npages_body_m)
            npages_body_m = re.sub(r"\.\.\.","",npages_body_m)
        else:
            npages_body_m = re.sub(r"&[^;]*;","",npages_body_m)
            npages_body_m = re.sub(r'Страницы:','',npages_body_m)       
    
        hospitals = find_where(get_body(link), '<!-- конец спешал размещения-->', '<tr><td colspan="2" style="text-transform: uppercase;">')   
        count_hospitals = spy_massiv(hospitals, '<a class')                 # how many hospitals on a page
        for l in xrange(count_hospitals): 
            link_hosp = find_where(hospitals,'href=\"','\">')               # links to hospitals
            link_hosp = re.sub(r'href=\"',' http://medfirm.ru',link_hosp)
            body_hosp = get_body(link_hosp)             
            name_h = find_where(body_hosp, '<h1>', '</h1>')
            name_h = re.sub(r'<h1>','',name_h)  
            name_h = name_h.strip()                                                 # name of organization
            address_h = find_where(body_hosp, '<b>Адрес:</b>', '<br><b>Телефон:')  
            address_h = re.sub(r'<b>Адрес:</b>', '', address_h)  
            address_h = address_h.strip()                                           # address of organization
            phone_h = find_where(body_hosp, '<br><b>Телефон:', '<b>Вид деятельности:') 
            phone_h = clear(phone_h, '')
            phone_h = re.sub(r'Телефон:', '', phone_h)
            phone_h = phone_h.strip()                                               # phone of organization
            worktype_h = find_where(body_hosp, '<b>Вид деятельности:', '') 
            worktype_h = re.sub(r'<b>Вид деятельности:','',worktype_h)
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
        
        
        