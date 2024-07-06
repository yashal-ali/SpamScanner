import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

import numpy as np

def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    ps=PorterStemmer()
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english')  and i not in string.punctuation:
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)
    
tfidf= pickle.load(open('vectorizer.pkl', 'rb'))
model_1 = pickle.load(open('model.pkl', 'rb'))

st.title('Email Analysis')
st.write('This app predicts the category of an email spam or not')
input_sms=st.text_area('Enter the email content in the box below')
if st.button('Predict'):
    transform_email=transform_text(input_sms)
    vector_input=tfidf.transform([transform_email])
    result= model_1.predict(vector_input)[0]
    if result==1:
        st.header('Spam')
    else:
        st.header('Not Spam')


