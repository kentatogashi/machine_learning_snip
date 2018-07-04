from sklearn.base import BaseEstimator, TransformerMixin, ClassifierMixin
import MeCab

# fit_transform
class JapaneseVectorizer(BaseEstimator, TransformerMixin):
    def __init__(self, opt='-Owakati'):
        self.opt = opt

    def transform(self, doc):
        tagger = MeCab.Tagger(self.opt)
        parsed = tagger.parse(doc)
        vect_dict = {}
        for word in parsed.split(' '):
            if word == '\n':
                continue
            if word in vect_dict:
                vect_dict[word] += 1
            else:
                vect_dict[word] = 1
        return vect_dict 

    def fit(self, x, Y=None):
        return self

doc = 'ウィキペディアは誰でも編集できるフリー百科事典です。'
vectorizer = JapaneseVectorizer()
print(vectorizer.get_params())
vect_dict = vectorizer.fit_transform(doc)
print(vect_dict)
"""
{'フリー': 1, '事典': 1, 'できる': 1, '誰': 1, '編集': 1, 'です': 1, 'でも': 1, 'ウィキペディア': 1, 'は': 1, '。': 1, '百科': 1}
"""

class JapaneseClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self):
        pass
