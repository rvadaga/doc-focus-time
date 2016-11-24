# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 22:12:02 2016

@author: shashank
"""

from bs4 import BeautifulSoup
#import re
import urllib
import urllib2
import justext
import requests
import lxml.html
linklist=[]
import datetime

e = 1
for i in range (41172,41213):
#    print i 
    
#    print "++++++++++++++++++++++++++=============++++++++++++=============="
    x = i - 40909
    d= datetime.date(2011,1,1)
    n = datetime.timedelta(x)
    day = d + n
    print day.strftime("%b-%d-%Y")
    toi = 'http://timesofindia.indiatimes.com/2016/11/2/archivelist/year-2016,month-11,starttime-' + str(i) + '.cms'
    try:
            
        linkceck = urllib2.Request(toi)
        linkcheck = urllib2.urlopen(linkceck)
        dom1 =  lxml.html.fromstring(linkcheck.read())
        l = dom1.xpath('//a/@href')
        for link in l:
            link = str(link)
            if 'articleshow' in link:
                
                if link[0] != 'h':
                    
    #                print link
    #                linka = 'http://timesofindia.indiatimes.com' + link
    #                linklist.append(linka)
                    continue
                else:
                    linklist.append(link)
    except:
        print "Connection Lost to TOI"
        pass
#    print linklist[1:55]
    for uri in linklist:
        try:
            response = requests.get(uri,timeout=1)
            paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
            fi = str(day.strftime("%d-%b")) +'-'+ str(e) + '.txt'
            f = open(fi, 'w+')
#        print day.strftime("%b-%d-%Y")
            f.write(str(day.strftime("%b-%d-%Y")))
            f.write('\n')
#            print len(paragraphs),uri,e
            for paragraph in paragraphs:
#                print paragraph.text
                if not paragraph.is_boilerplate:
                    if paragraph.text == 'RELATED' or paragraph.text == 'Comments' or paragraph.text=='Stay updated on the go with Times of India News App. Click here to download it for your device.'  or paragraph.text == 'From around the web':
    #                    print paragraph.text
                        break
                    
    #                print paragraph.text
                    f.write(( paragraph.text).encode('ascii', 'ignore'))
                    f.write('\n')
            f.close()
        except:
#            print "No Page = " , uri, '==',e
            pass
        e = e + 1

    del linklist[:]
#response = requests.get('http://timesofindia.indiatimes.com/hyderabad-times/Mega-millennium-cultural-fest/articleshow/1636705548.cms?')
#paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
#
#for paragraph in paragraphs:
#    if not paragraph.is_boilerplate:
#        print paragraph.text

#import datetime
#day_of_year = datetime.date(2001,4,30).timetuple().tm_yday
#print day_of_year
#
#print day_of_year + 36892
#
#print (15*365) + 36892
