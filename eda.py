import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from PIL import Image

def run():
    st.write('# FIFA PLAYER RATING')

    # load
    gambar = Image.open('Ringkasan Statistik Deskriptif .jpg')
    st.write(gambar)

    st.write('# Description')

    st.write('''Menurut laporan FIFA 2022, jumlah pemain sepak bola pada tahun 2022 kurang lebih sebanyak 100.000 pemain. 
            Namun, dalam dataset ini yang digunakan hanya mencakup 20.000 pemain saja. Project ini bertujuan untuk 
            memprediksi rating pemain FIFA 2023 sehingga semua pemain sepak bola profesional dapat diketahui rating nya 
            dan tidak menutup kemungkinan akan lagir wonderkid baru. Project ini akan dibuat menggunakan algoritma Linear 
            Regresison dan dievaluasi dengan metrics MAE sebagai pertimbangan.''')

    # load data
    df = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/master/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')

    st.write('# Dataset')
    # menampilkan dataframe
    st.write(df)

    # membuat visualisasi (grafik)
    st.write('# Exploratory Data Analysis')

    st.write('## Distribution of Player Rating')

    # plot harus diawali dengan variable figure
    fig = plt.figure(figsize = (16,5))
    sns.histplot(df['Overall'], kde = True, bins = 30)
    plt.title('Distribution of Rating')
    # untuk nampilin pakai st.pyplot(fig)
    st.pyplot(fig)

    st.write('''insight: Terlihat dari histogram, 
            Rating terdistribusi normal dengan rata-rata di sekitar 65.
            Tinggi dan berat badan pemain mempunyai korelasi yang positif, 
            semakin besar tinggi badan pemain makan berat badan pemain juga semakin besar. 
            Sehingga bisa dibilang bahwa pemain sepak bola pada dataset ini proporsional.
            ''')

    st.write('## Histogram berdasarkan Input')

    option = st.selectbox(
        label = "Input field yang mau divisualisasikan",
        options = ['PaceTotal', 'ShootingTotal', 'PassingTotal',
                'DribblingTotal', 'DefendingTotal', 'PhysicalityTotal'])

    fig = plt.figure(figsize = (16,5))
    sns.histplot(df[option], kde = True, bins = 30)
    plt.title(f'Distribution of {option}')
    # untuk nampilin pakai st.pyplot(fig)
    st.pyplot(fig)

    # visualisasi plotly
    st.write('## Tinggi vs Berat Pemain')
    chart = px.scatter(df, 'Height', 'Weight')
    st.plotly_chart(chart)

if __name__ == '__main__':
    run()
