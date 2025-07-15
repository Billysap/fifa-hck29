import eda, prediction
import streamlit as st

with st.sidebar:
    st.write('# Page Navigation')

    page = st.selectbox('Pilih Halaman',
                       ['EDA', 'Predict Rating'])
    
    st.write('# About')
    st.write('''Page ini berisikan''')

if page == 'EDA':
    eda.run()

else:
    prediction.run()