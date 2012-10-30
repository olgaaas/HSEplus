# -*- coding: utf-8 -*-

'''
Copyright © Alexey Khan 2012  All rights reserved
09.08.12; web-pages parsing library;
'''

#Library
import httplib, sys, re
import locale, urllib, urllib2, random

#Function Get body
def get_body(url):
    html = urllib.urlopen(url)
    html = html.read()
    return html

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
def clear(perem,change = None):
    if change == None:
        perem = re.sub(r"<[^>]*>","",perem)
        
    else:
        perem = re.sub(r"<[^>]*>",change,perem)
    perem = re.sub(r"\n",change,perem)
    perem = re.sub(r"\r",change,perem)
    perem = re.sub(r"\t",change,perem)
    perem = re.sub(r"&quot;","\"",perem)
    perem = re.sub(r"&laquo;","\"",perem)
    perem = re.sub(r"&raquo;","\"",perem)
    perem = re.sub(r"&nbsp;"," ",perem)
    perem = re.sub(r"&amp;","&",perem)
    perem = re.sub(r"&ndash;",":",perem) 
    perem = re.sub(r"&#150;","-",perem) 
    
    
    return perem

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
                print country

                status = "ok"
            
        if url is not None:
                
            page_request = urllib2.Request(url, headers = headers)
                
            try:
                data = urllib2.urlopen(page_request).read()               
            except(IOError), msg: 
                
                errors = {"404":"NOT such page",
                          "400":"Syntaxis",
                          "500":"Socet",
                          "504":"Server error or in url"}
                #print msg
                
                cur_error = get_field(str(msg),"Error ",":")
                cur_error = re.sub(r"Error ","",cur_error)
                
                print errors[cur_error]
                
                status = "ok"
                
            else:
                
                status = "ok"
                return data
            
def get_url(html,b_url,e_url,link):
    url_mas = []
    count_url = spy_massiv(html,b_url)
    for o in range(count_url):
        url = find_where(html,b_url,"\">")
        url = re.sub(r""+b_url+"",link,url)
        html = find_where(html,b_url,"")
        url_mas.append(url)
    return url_mas