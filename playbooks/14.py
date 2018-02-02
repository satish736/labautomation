#!/usr/bin/python 

import nltk   
from urllib import urlopen

url = "https://downloads.chef.io/chef-server/stable"    
html = urlopen(url).read()    
raw = nltk.clean_html(html)  
print(raw)