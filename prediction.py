#Import library
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

#Load all files

with open('list_cat_cols.txt', 'r') as file_1:
  list_cat_cols = json.load(file_1)

with open('list_num_cols.txt', 'r') as file_2:
  list_num_cols = json.load(file_2)

with open('scaler.pkl', 'rb') as file_3:
  scaler = pickle.load(file_3)

with open('encoder.pkl', 'rb') as file_4:
  encoder = pickle.load(file_4)

with open('linreg.pkl', 'rb') as file_5:
  model_lin_reg = pickle.load(file_5)

with open('model.pkl', 'rb') as file_6:
  model = pickle.load(file_6)

def run():
    with st.form('form_player'):
      st.write('Isi dengan data pemain')
      name = st.text_input('Nama Player')
      age = st.number_input('Usia Player', min_value= 17)
      height = st.number_input('Tinggi Player', min_value=100, 
                              max_value = 300, value = 160)
      weight = st.number_input('Berat Player', min_value=40)
      price = st.number_input('Harga Player', min_value = 0)

      options = ['Low', 'Medium', 'High']
      attacking_rate = st.selectbox('Attacking work rate',
                                    options = options)
      defending_rate = st.selectbox('Defensive work rate',
                                    options = options)
      
      pace = st.slider('Pace', min_value=0, max_value=100)
      shooting = st.slider('Shooting', min_value=0, max_value=100)
      passing = st.slider('Passing', min_value=0, max_value=100)
      dribbling = st.slider('Dribbling', min_value=0, max_value=100)
      defending = st.slider('Defending', min_value=0, max_value=100)
      physicality = st.slider('Physicality', min_value=0, max_value=100)
      
      submit = st.form_submit_button()

    data_inf = {
        'Name': name,
        'Age' : age,
        'Height' : height,
        'Weight' : weight,
        'Price' : price,
        'AttackingWorkRate': attacking_rate,
        'DefensiveWorkRate': defending_rate,
        'PaceTotal': pace,
        'ShootingTotal': shooting,
        'PassingTotal': passing,
        'DribblingTotal': dribbling,
        'DefendingTotal': defending,
        'PhysicalityTotal': physicality
    }

    data_inf = pd.DataFrame([data_inf])
    #Split between numerical columns and categorical columns

    data_inf_num = data_inf[list_num_cols]
    data_inf_cat = data_inf[list_cat_cols]

    #Feature scaling and feature encoding

    data_inf_num_scaled = scaler.transform(data_inf_num)
    data_inf_cat_encoded = encoder.transform(data_inf_cat)
    data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded], axis = 1)

    if submit:
        prediction = model_lin_reg.predict(data_inf_final)
        st.write(f'# Predicted Rating: {prediction[0]}')

        prediction2 = model.predict(data_inf)
        st.write(f'# Predicted Rating: {prediction2[0]}')

if __name__ == '__main__':
    run()