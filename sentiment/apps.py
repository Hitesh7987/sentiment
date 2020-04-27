from django.apps import AppConfig
import numpy as np
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import gensim
import pickle

class SentimentConfig(AppConfig):
    name = 'sentiment'
    forest = ''
    model = ''
    num_workers = 4
    num_features = 300
    context = 10
    min_word_count = 40
    downsampling = 1e-3
    def ready(self):
        print("Logging message")
      #  self.model = gensim.models.Word2Vec.load('sentiment/300fea_40work_10cont')
       # self.forest = pickle.load(open('sentiment/random_forest_model2', 'rb'))
        pass

    def getSentiment(self,text):
        test_review = []
        test_review.append(review_wordlist(text, remove_stopwords=True))
        test_vecs = getAvgFeaturevecs(test_review, self.model, self.num_features)
        return self.forest.predict(test_vecs)[0]


def review_wordlist(review, remove_stopwords=False):
    review_text = BeautifulSoup(review,features="html.parser").get_text()
    review_text = re.sub('[^a-zA-Z]', ' ', review_text)
    words = review_text.lower().split()
    if remove_stopwords:
        stops = set(stopwords.words('english'))
        words = [w for w in words if not w in stops]
    return words

# function to average all words in a particular sentence
def featureVecMethod(words, model, num_features):
    featureVec = np.zeros(num_features, dtype='float32')
    nwords = 0

    # convertind indexes to word
    word_set = model.wv.index2word

    for word in words:
        if word in word_set:
            featureVec = np.add(featureVec, model[word])
            nwords = nwords + 1

    # dividing to get an average
    featureVec = np.divide(featureVec, nwords)
    return featureVec

# fucntion for calcuating average feature vector
def getAvgFeaturevecs(reviews, model, num_features):
    featureVecs = np.zeros((len(reviews), num_features), dtype='float32')
    counter = 0

    for review in reviews:
        featureVecs[counter] = featureVecMethod(review, model, num_features)
        counter = counter + 1
    return featureVecs

