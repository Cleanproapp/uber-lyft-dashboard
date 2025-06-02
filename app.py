
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Uber/Lyft", layout="wide")
st.title("🚗 Painel Uber/Lyft")

uploaded_file = st.file_uploader("📁 Faça upload do arquivo CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Prévia dos Dados")
    st.dataframe(df.head())

    if 'start_time' in df.columns:
        df['start_time'] = pd.to_datetime(df['start_time'])
        df['hour'] = df['start_time'].dt.hour
        st.subheader("📊 Corridas por Hora")
        st.bar_chart(df['hour'].value_counts().sort_index())
