import streamlit as st
import joblib
model_nb = joblib.load('Ecom_fraud_det')
st.title('Ecom_fraud_det') #creates a title in web app
ip = st.number_input('Enter input:') #creates a text box in web app
op = model_nb.predict([[ip]])
if st.button('Predict'):
  st.title(op[0])
               
             
