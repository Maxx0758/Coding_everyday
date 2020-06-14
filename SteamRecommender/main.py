import sklearn
import pandas as pd
import math
import random
import sklearn
from nltk.corpus import stopwords
from scipy.sparse import csr_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse.linalg import svds
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

"""Loading the data sheet and collects all individual apps"""
steamgames = pd.read_csv('steam_games.csv')
steamgames = steamgames[steamgames['types'] == 'app']
# print(steamgames)
# print(steamgames.head())

"""Giving weight to different types"""

'''
type_strength = {
    'recent_reviews': 3.0, 
    'all_reviews': 3.0,
    'popular_tags': 2.0,
    'developer': 1.0,
    'publisher': 1.0,
    'original_price': 1.0
}
'''

recent_reviews = {
    'Overwhelmingly Positive': 4.0,
    'Very Positive': 3.0,
    'Positive': 2.0,
    'Mostly Positive': 1.0,
    'Mixed': 0.0,
    'Mostly Negative': -1.0,
    'Negative': -2.0
}

all_reviews = {
    'Overwhelmingly Positive': 4.0,
    'Very Positive': 3.0,
    'Positive': 2.0,
    'Mostly Positive': 1.0,
    'Mixed': 0.0,
    'Mostly Negative': -1.0,
    'Negative': -2.0
}

def gayness(x):
    print(f'gayness = {x}')
    if type(x) != float:
        k = x.split(',')[0]
    return recent_reviews[k]

def feminest(x):
    print(f'feminestness = {x}')
    if type(x) != float:
        k = x.split(',')[0]
    return all_reviews[k]
# """Number of games"""
# k = len(steamgames['name'])
# print("There are this many games: {}".format(k))


# # print(len(steamgames['recent_reviews'][6]))
# # print(steamgames['recent_reviews'][6])


"""Giving a weight to recent_review"""

for rreview in steamgames['recent_reviews']:
    if type(rreview) != float:
        r = rreview.split(',')
        if r[0] in recent_reviews and r[0] != 'NaN': 
            print(f'first r[0] {r[0]}')
            print(f'recent_reviews {recent_reviews[r[0]]}')
        else:
            break
        
steamgames['reviewStrength2'] = steamgames['recent_reviews'].apply(
    lambda x: gayness(x))
print(steamgames['reviewStrength2'])




"""Giving a weight to all_review"""

for areview in steamgames['all_reviews']:
    if type(areview) != float:
        r = areview.split(',')
        if r[0] in all_reviews and r[0] != 'NaN': 
            print(f'second r[0] {r[0]}')
            print(f'all_reviews {all_reviews[r[0]]}')
        else:
            break

steamgames['reviewStrength1'] = steamgames['all_reviews'].apply(
    lambda x: feminest(x))
print(steamgames['reviewStrength1'])
