# News Category Prediction

This model is designed and developed to predict the category of the news. The categories that this can identify are Politics,  Technology, Entertainment and Business.
Model is developed and deployed using Flask api. Below is the url where you can predict your news category.

https://newscategorypredictor.herokuapp.com/

## Overview
The **News Category Prediction** project is a machine learning model designed to classify news articles into predefined categories based on their content. This project is hosted online and accessible via the following URL:
[News Category Predictor](https://newscategorypredictor.herokuapp.com/).

## Features
- **Text Classification**: Predicts the category of a given news article.
- **User-Friendly Interface**: Simple and intuitive design for inputting and classifying news articles.
- **Multi-Category Support**: Handles multiple news categories efficiently.
- **Interactive Deployment**: Hosted as a web application for easy accessibility.

## Technologies Used
- **Programming Language**: Python
- **Libraries and Frameworks**:
  - **Text Preprocessing**: NLTK, SpaCy
  - **Vectorization**: CountVectorizer
  - **Model Building**: Scikit-learn (Logistic Regression, Naïve Bayes, or similar models)
  - **Web Framework**: Flask
  - **Deployment**: Heroku
- **Dataset**: News articles dataset from publicly available sources (e.g., Kaggle, UCI ML Repository).

## How It Works
1. **Data Preprocessing**:
   - Tokenization, stopword removal, and stemming/lemmatization.
   - Convert text data to numerical form using Count vectorization.
2. **Model Training**:
   - Train a classification model using labeled news data.
3. **Prediction**:
   - Predict the category of new articles based on the trained model.
4. **Web Application**:
   - Deploy the model on Heroku using a Flask-based web interface.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd news-category-prediction
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Flask app locally:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```
3. Input a news article's text and get the predicted category.

Alternatively, you can access the live application here: [News Category Predictor](https://newscategorypredictor.herokuapp.com/).

## Dataset
The dataset includes labeled news articles with categories such as Politics, Sports, Technology, Entertainment, etc. Preprocessing steps were applied to clean and prepare the data.

## Future Enhancements
- Incorporate deep learning techniques (e.g., LSTM, BERT) for improved accuracy.
- Add multilingual support for news articles.
- Enhance the UI for a better user experience.
- Implement real-time predictions using streaming data.


