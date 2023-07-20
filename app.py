import streamlit as st
import pandas as pd


st.title("****App to predict the defaults****")

df = pd.read_csv('Model_results.csv')
if st.button("Predict"):
    st.write(df)
    
    
        
   
    
