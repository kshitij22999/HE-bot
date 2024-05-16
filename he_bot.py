# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 08:50:15 2024

@author: Kshitij
"""

import requests
import re
import csv

email_reg=r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])''' 
keywords='media'
media_mails={}
mails={}
urls = open('D:\\demo.txt', mode='r', newline='').read().rstrip('\n').split()
print(urls)  
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',}



for url in urls:
    #spamreader = csv.reader(urls, delimiter='\n', quotechar='|')
    print(url)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.status_code)
    else:
        print(f'Request failed with status code: {response.status_code}')
    
    #body_ref=response.text.find("<body")
    ref = response.text.lower().find('media')
    print(ref)
    if ref>=0:
        #for re_match in re.search(email_reg,response.text[ref:ref+500]):
        re_match=re.search(email_reg, response.text[ref:])
        media_mails[url]=re_match.group()
    else:
        print('this is running')
        for re_match in re.finditer(email_reg,response.text):
            if url in mails:
                mails.get(url).add(re_match.group())
            else:
                mails[url]=set(re_match.group())
        
    
    #ref = response.text.lower().find(keywords)
    
    
    
print(media_mails)
print(mails)
