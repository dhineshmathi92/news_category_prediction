# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 09:33:29 2021

@author: Dhinesh M

"""
from flask import Flask, render_template, request
import pickle
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemma = WordNetLemmatizer()


app = Flask(__name__)

vector = pickle.load(open('countvector.pkl','rb'))
model = pickle.load(open('NBmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        tokens = word_tokenize(message)
        nonstop_token = [word for word in tokens if word.casefold() not in stopwords.words('english') and word.isalnum()]
        lemmas = ' '.join([lemma.lemmatize(token) for token in nonstop_token])
        input = vector.transform([lemmas]).toarray()
        output = model.predict(input)
        
        return render_template('results.html', prediction=output)



if __name__ == '__main__':
    app.run(debug=True)

