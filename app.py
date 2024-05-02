import streamlit as st 
import joblib


model=joblib.load('news-classification-model.pkl')

news_labels={0:"Technical",1:"Business",2:'Sports',3:'Entertainment','4':'Politics'}

st.title('News Classification')
user_input=st.text_area('Enter news here:')
if st.button('Predict'):
    predicted_sentiment=model.predict([user_input])[0]
    print(predicted_sentiment)
    predicted_sentiment_label=news_labels[predicted_sentiment]

    st.info(f'Predicted Sentiment: {predicted_sentiment_label}')