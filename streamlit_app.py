import streamlit as st
import pandas as pd
st.title('🤖 Machine Learning App')

st.info('This is app is built on machine learning model')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/087cb5383af3b09e68f6eeb00dea8819c1340de0/penguins_size.csv')

