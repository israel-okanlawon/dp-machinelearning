import streamlit as st
import pandas as pd
st.title('🤖 Machine Learning App')

st.info('This is app is built on machine learning model')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/087cb5383af3b09e68f6eeb00dea8819c1340de0/penguins_size.csv')
  df

  st.write('**X**')
  X = df.drop('species', axis=1)
  X
  
  st.write('**y**')
  y = df['species']
  y
