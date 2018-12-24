#! /usr/bin/python3
# Runs with Python 3
#import needed stuff
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

#suppress warnings
import warnings
warnings.filterwarnings("ignore")

# Add more stopwords to the list:
stopwords = set(STOPWORDS)
stopwords.update(["Update", "details", "App", "Used", "use", "splitsen", "might", "naar", "verschillende"])

#open file with all the URLs to scrape
with open('weblist.txt', encoding='utf-8-sig') as f:
    weblist = [line.strip() for line in f]

#For each line in the weblist, scrape de site and dump it to text_raw
wiki_raw = ''
for list in weblist:
    url = urlopen(list)
    soup = BeautifulSoup(url)
    #remove TOC header
    soup.find('div', id="header").decompose()
    #remove TOC sidebar
    soup.find('div', id="toc").decompose()
    #If h2,h3,h4,h5 (removing chapter text)
    if soup.find('h2'):
        soup.find('h2').decompose()
    if soup.find('h3'):
        soup.find('h3').decompose()
    if soup.find('h4'):
        soup.find('h4').decompose()
    if soup.find('h5'):
        soup.find('h5').decompose()
    for s in soup(['script', 'style']):
        s.decompose()
    raw_soup = ' '.join(soup.stripped_strings)
    wiki_raw += raw_soup

# Massive cleanup Raw text
clean_wiki = wiki_raw
clean_wiki = ' '.join(word for word in clean_wiki.split(' ') if not word.startswith('http'))
clean_wiki = ' '.join(word for word in clean_wiki.split(' ') if not word.startswith('www'))
clean_wiki = ''.join([i for i in clean_wiki if not i.isdigit()])
clean_wiki = re.sub(r'[^A-Za-z]', ' ', clean_wiki)
clean_wiki = ' '.join( [w for w in clean_wiki.split() if len(w)>1] )
clean_wiki = clean_wiki.replace('UTC',' ')
clean_wiki = re.sub(' +',' ',clean_wiki)

#Import Black and White shape of Willy
willy_shape = np.array(Image.open("bwavatar.png"))

# Create a word cloud image
wc = WordCloud(background_color="white", max_words=1500, mask=willy_shape,
               stopwords=stopwords,min_font_size=4, contour_width=5, contour_color='gainsboro')

# Generate a wordcloud
wc.generate(clean_wiki)

# store to file
wc.to_file("/var/www/html/willywordcloud.png")


# show
plt.figure(figsize=[20,10])
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
