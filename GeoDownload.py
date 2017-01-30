# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 19:44:18 2017

@author: the4960
"""
import requests
import urllib

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

max = 38
posts = []
for page in range(1,max+1):
    url = "http://geometrydaily.tumblr.com/page/"+str(page)
    response = requests.get(url)
    if response.status_code != 200:
        print 'GOT ! 200'
        break
    for line in response.content.split('\n'):
        if 'href="' in line:
            splitter = line.split('href="')
            for elem in splitter:
                if ('>' in elem) and 'http://geometrydaily.tumblr.com/' in elem:
                    elem = elem[:elem.index('">')]
                    if elem.index('http://geometrydaily.tumblr.com/') == 0 and '/post/' in elem:
                        posts.append(elem)
    #print("NEW PAGE NEW PAGE NEW PAGE NEW PAGE\n")
    
for page in posts:
    #print(page+".....NEWPAGE NEWPAGE NEWPAGE\n")
    response = requests.get(page)
    if response.status_code != 200:
        print 'GOT ! 200'
        break
    for line in response.content.split('\n'):
        if '<div class="index"><div class="detail">' in line:
            splitter = line.split('<div class="index"><div class="detail">')
            elem = find_between( splitter[1],'src="','" style=')
            name = elem.split("/")[-1]
            print(elem+"\n")
            urllib.urlretrieve(elem, "geom/"+name)
    
print("END END END END")
