import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv(
    r'C:\Users\chris\OneDrive\Documents\Data_Analyst\Sprint 5\sprint5_project\vehicles_us.csv')  # leer los datos


st.header('Información de vehículos')
hist_button = st.button('Construir histograma')
dispersion_button = st.button('Construir gráfico de dispersion')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")  # crear un histograma

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if dispersion_button:  # al hacer click en el botón
    st.write('Creación del gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches')

    # crear histograma
    fig = px.scatter(car_data, x="odometer", y="price")

    # montrar el gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
