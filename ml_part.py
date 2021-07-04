import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial import distance
import json
from voice import talk,take_command

with open('intent.json') as json_data:
    data = json.load(json_data)
data = data['intents']


dataset = pd.DataFrame(columns=['intent', 'text', 'response'])
for i in data:
    intent = i['intent']
    for t, r in zip(i['text'], i['responses']):
        row = {'intent': intent, 'text': t, 'response':r}
        dataset = dataset.append(row, ignore_index=True)


def cosine_distance_countvectorizer_method(s1, s2):
    
    # sentences to list
    allsentences = [s1 , s2]
    
    # packages
    from sklearn.feature_extraction.text import CountVectorizer
    from scipy.spatial import distance
    
    # text to vector
    vectorizer = CountVectorizer()
    all_sentences_to_vector = vectorizer.fit_transform(allsentences)
    text_to_vector_v1 = all_sentences_to_vector.toarray()[0].tolist()
    text_to_vector_v2 = all_sentences_to_vector.toarray()[1].tolist()
    
    # distance of similarity
    cosine = distance.cosine(text_to_vector_v1, text_to_vector_v2)
    return round((1-cosine),2)


def respond(voice_data):
    maximum = float('-inf')
    response = ""
    closest = ""
    for i in dataset.iterrows():
        sim = cosine_distance_countvectorizer_method(voice_data, i[1]['text'])
        if sim > maximum:
            maximum = sim
            response = i[1]['response']
            closest = i[1]['text']
    return response
