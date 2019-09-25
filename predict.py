def classifier():
    import pandas as pd
    import re
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    from nltk.stem import WordNetLemmatizer
    from sklearn.tree import DecisionTreeClassifier
    import pickle
    import numpy as np
    import matplotlib.pyplot as plt

    testdata = pd.read_csv('q1.csv')
    value = len(testdata.index)
    loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
    corpus = []
    for i in range(0, value):
        review = re.sub('[^a-zA-Z]', ' ', testdata['SentimentText'][i])
        review = review.lower()
        review = review.split()
        sno = nltk.stem.SnowballStemmer('english')
        lemma = WordNetLemmatizer()
        ps = PorterStemmer()
        review = [lemma.lemmatize(word)
                  for word in review if not word in set(stopwords.words('english'))]
        review = ' '.join(review)
        corpus.append(review)
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(max_features=605)
    X = cv.fit_transform(corpus).toarray()
    y_pred = loaded_model.predict(X)
    positive = 0.0
    negative = 0.0
    q1_score = 0.0
    for j in range(0, value):
        if(y_pred[j] == 1):
            positive = positive+1
        else:
            negative = negative+1
    #print 'Modi_Positive',positive
    #print 'Modi_Negative',negative

    testdata2 = pd.read_csv('q2.csv')
    value2 = len(testdata2.index)

    corpus = []
    for i in range(0, value2):
        review2 = re.sub('[^a-zA-Z]', ' ', testdata2['SentimentText'][i])
        review2 = review2.lower()
        review2 = review2.split()
        sno = nltk.stem.SnowballStemmer('english')
        lemma = WordNetLemmatizer()
        ps = PorterStemmer()
        review2 = [lemma.lemmatize(word)
                   for word in review2 if not word in set(stopwords.words('english'))]
        review2 = ' '.join(review2)
        corpus.append(review2)
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(max_features=605)
    X2 = cv.fit_transform(corpus).toarray()
    y_pred2 = loaded_model.predict(X2)
    positive2 = 0.0
    negative2 = 0.0
    q2_score = 0.0
    for j in range(0, value2):
        if(y_pred2[j] == 1):
            positive2 = positive2+1
        else:
            negative2 = negative2+1
    #print 'RaGa_Positive',positive2
    #print 'RaGa_Negative',negative2

    return positive, negative, positive2, negative2
