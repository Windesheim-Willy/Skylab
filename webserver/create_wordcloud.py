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

#Open file with all the blocked words:
stopwords = set(line.strip() for line in open('stopwords.txt'))

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

# Open file with Wordcloud variables from file
with open('cloudset.txt', encoding='utf-8-sig') as f:
    cloudset = [line.strip() for line in f]

# Convert line of list to string and search for 'starting' var to set to var
bgcolor = ''.join([s for s in cloudset if "bgcolor" in s])
if bgcolor.startswith('bgcolor'):
    bgcolor = bgcolor[8:]

max_words = ''.join([s for s in cloudset if "max_words" in s])
if max_words.startswith('max_words'):
    max_words = int(max_words[10:])

min_font_size = ''.join([s for s in cloudset if "min_font_size" in s])
if min_font_size.startswith('min_font_size'):
    min_font_size = int(min_font_size[14:])

contour_width = ''.join([s for s in cloudset if "contour_width" in s])
if contour_width.startswith('contour_width'):
    contour_width = int(contour_width[14:])

contour_color = ''.join([s for s in cloudset if "contour_color" in s])
if contour_color.startswith('contour_color'):
    contour_color = contour_color[14:]

# Create a word cloud image
wc = WordCloud(background_color=bgcolor, max_words=max_words, mask=willy_shape,
               stopwords=stopwords, min_font_size=min_font_size, contour_width=contour_width,
               contour_color=contour_color)

# Generate a wordcloud
wc.generate(clean_wiki)

# store to file
wc.to_file("/var/www/html/willywordcloud.png")

# show
plt.figure(figsize=[20,10])
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
