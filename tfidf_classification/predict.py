# Idea https://towardsdatascience.com/machine-learning-nlp-text-classification-using-scikit-learn-python-and-nltk-c52b92a7c73a
# Data https://www.kaggle.com/rtatman/deceptive-opinion-spam-corpus 
# Desc predict polarity and deceptive rate.

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

df = pd.read_csv('deceptive-opinion.csv')
# print(df.head())
X_train, X_test, y_train, y_test = train_test_split(df.text, df.polarity, test_size=0.3)
text_clf = Pipeline([('vec', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])
text_clf = text_clf.fit(X_train, y_train)
predicted = text_clf.predict(X_test)
print('predict polarity correct rate')
print(np.mean(predicted == y_test))

X_train, X_test, y_train, y_test = train_test_split(df.text, df.deceptive, test_size=0.3)
text_clf = Pipeline([('vec', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])
text_clf = text_clf.fit(X_train, y_train)
predicted = text_clf.predict(X_test)
print('predict deceptive correct rate')
print(np.mean(predicted == y_test))
