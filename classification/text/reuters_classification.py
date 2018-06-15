#!/root/miniconda3/bin/python
# -*- coding: utf-8 -*-

import os
import time
import requests
import re
import pandas as pd
import numpy as np
from os.path import abspath, dirname, isfile
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

URL_TEMPLATE = 'https://www.reuters.com/resources/archive/jp/%s.html'
DATA_DIR = abspath(dirname(__file__)) + '/data'
DATA = DATA_DIR + '/data.txt'

def dtr(s, e):
    for i in range((e - s).days):
        yield s + timedelta(i)

def fetch_archive(day):
    url = URL_TEMPLATE % day
    filepath = DATA_DIR + '/' + day + '.txt'
    if isfile(filepath):
        print('Already exists %s ...' % url)
        return
    print("Fetching %s..." % url)
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    headers = soup.find('div', attrs={'class': 'module'}).find_all('a')
    fall = open(DATA, 'a')
    with open(filepath, 'a') as f:
        for header in headers:
            line = header.getText() + '\n'
            f.write(line)
            fall.write(line)
    fall.close()
    time.sleep(3)

def make_datasets():
    s = datetime.strptime('20180601', '%Y%m%d')
    e = datetime.strptime('20180614', '%Y%m%d')
    os.makedirs(DATA_DIR, exist_ok=True)
    for i in dtr(s, e):
        fetch_archive(datetime.strftime(i, '%Y%m%d'))

def load_datasets():
    return [i.rstrip('\n') for i in open(DATA).readlines()]

def preprocess(datasets, stop_words):
    train  = [re.sub(r'[0-9]', '0', i) for i in datasets]
    tf_vect = TfidfVectorizer(stop_words = stop_words)
    return tf_vect.fit_transform(train)

def classify(datasets, n_clusters = 100, stop_words = []):
    km = KMeans(n_clusters=n_clusters, max_iter = 1000)
    train = preprocess(datasets, stop_words)
    km.fit(train)
    return km.labels_

if __name__ == '__main__':
    make_datasets()
    datasets = load_datasets()
    n_clusters = 100
    stop_words = ['UPDATE', 'マーケットアイ', '焦点', '再送', 'アングル']
    label = classify(datasets, n_clusters = n_clusters, stop_words = stop_words)
    df = pd.DataFrame(datasets, columns=['header'])
    for i in range(n_clusters):
        print(df.iloc[label == i, [0]].head(10))
