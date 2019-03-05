#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 20:23:17 2019

@author: Farhad
"""

import requests
from bs4 import BeautifulSoup
import re
from dask import delayed
import sys
import csv


print('Yahoo_finacial_search(words,savefile)')
print(" ")
print('csv file save automate')
print('output: self.titles_list')
print("----------------------------------------------------------")







def EstimateFaster(num,xlist, description):
    """
    Estimate length of loop and time 
    """
    num+=1
    run = ("["+str(num)+'/'+str(len(xlist))+"]["+str(description)+']')
        
    sys.stdout.write('\r'+ run)

def Yahoo_finacial_search_topic(words):
    """
    funcation:
    search in Yahoo financial website and looking for the news that match with oure 
    worsd and give url and title list of them 
    ______________________________________
    input:
           words: (list,str) it is a list of words we looking for them in titles of news
    ______________________________________
    output:
         titles_list: (dic, str) 
         1. url of titles news that match with words list
         2. title of news that match with words list
    """
    words = [x.lower() for x in words]
    topUrl = 'https://finance.yahoo.com/?guccounter=1'
    respfirst = requests.get( topUrl)
    soup = BeautifulSoup(respfirst.text, 'lxml')
    titles = soup.find_all('a', href=True)
    
    titles_list = {}
    titles_list['titles'] = []
    titles_list['url_titles'] = []
    for word in words:
        for tit in titles:
            m = re.search(word,tit.text.lower())
            
            if m is not None:
                titles_list['titles'].append(tit.text)
                titles_list['url_titles'].append(tit['href'])
    if titles_list is None:
        print("Don't have news about {}".foramt(words))
        return titles_list
    return titles_list
def Yahoo_finacial_search_subscript(titles_list):
    """
    funcation:
    get url and go to page and get all of main text of page relate with isuue
    ______________________________________
    input:
         titles_list: (dic, str) 
         1. url of titles news that match with words list
         2. title of news that match with words list
    ______________________________________
    output:
        titles_list: (dic, str) 
         1. url of titles news that match with words list
         2. title of news that match with words list
         3. main text relate to title and url
    """
    titles_list['main_text']= []
    titles_list['date'] = []
    for num,url in enumerate(titles_list['url_titles']):
        EstimateFaster(num,titles_list['url_titles'], 'number of news that are found ')
        resp_sec = requests.get('https://finance.yahoo.com{}'.format(url))
        soup_sec = BeautifulSoup(resp_sec.text,'lxml')
        body = soup_sec.find('body')
        date = soup_sec.find('time',{'itemprop':"datePublished"} ).text
        main_text = [x.text for x in body.find_all('p',{'type':'text'})]
        main_text = ' '.join(main_text[:])
        titles_list['main_text'].append(main_text)
        titles_list['date'].append(date)
    return titles_list
def Yahoo_finacial_search(words,savefile):
    """
    funcation:
    it search in finance.yahoo.com/news/ with speacial keywords.
    it is made from two fucnation,
        1. Yahoo_finacial_search_topic
        2. Yahoo_finacial_search_subsript
    ______________________________________
    input:
        words: (list,str) it is a list of words we looking for them in titles of news
    ______________________________________
    output: 
         1. a csv file of news that it collected 
         2. give a dictounary from news (title, url, main_text)
    """
   
    titles_list = delayed(Yahoo_finacial_search_topic)(words)
    main_text = delayed(Yahoo_finacial_search_subscript)(titles_list)
    titles_list = main_text.compute()
    with open (savefile,'a') as f:
        for num,col in enumerate(titles_list['titles']):
            file = csv.writer(f)
            llist =[str(titles_list['date'][num]),
                    str(titles_list['titles'][num]),
                    str(titles_list['url_titles'][num]),
                    str(titles_list['main_text'][num])]
            EstimateFaster(num,titles_list['url_titles'], 'number of news that are saved')
            file = file.writerow(llist)
    return titles_list