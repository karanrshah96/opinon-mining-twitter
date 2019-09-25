import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.tree import DecisionTreeClassifier

# nltk.download('stopwords')
# nltk.download('wordnet')
dataset = pd.read_csv('dataset.csv', encoding="ISO-8859-1")
corpus = []
for i in range(0, 4000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['SentimentText'][i])
    review = review.lower()
    review = review.split()
    sno = nltk.stem.SnowballStemmer('english')
    lemma = WordNetLemmatizer()
    ps = PorterStemmer()
    review = [lemma.lemmatize(word) for word in review if not word in set(
        stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=605)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[0:4000, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

filename = 'finalized_model.sav'
pickle.dump(classifier, open(filename, 'wb'))

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

from sklearn.metrics import accuracy_score
asd = accuracy_score(y_test, y_pred)
