import streamlit as st
import pandas as pd
import plotly.express as px

url = 'vehicles_us.csv'
car_data = pd.read_csv(url)  # leer los datos


st.header('Información de vehículos')
hist_button = st.button('Construir histograma')
dispersion_button = st.button('Construir gráfico de dispersion')
bar_checkbox = st.checkbox('Contruir un gráfico de barras')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")  # crear un histograma
    fig.update_layout(title='Gráfico kilometraje vs Cantidad de autos',
                      xaxis_title='Kilometraje', yaxis_title='Cantidad de autos')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if dispersion_button:  # al hacer click en el botón
    st.write('Creación del gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches')

    # crear histograma
    fig = px.scatter(car_data, x="odometer", y="price")
    fig.update_layout(title='Gráfico kilometraje vs precio',
                      xaxis_title='Kilometraje', yaxis_title='Precio')

    # montrar el gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)

if bar_checkbox:  # al hacer click en la casilla de verificación
    # escriibr mensaje
    st.write('Creación de un gráfico de barras')

    # creación de un gráfico de barras
    fig = px.bar(car_data, x="condition",
                 y="odometer",
                 color="condition",
                 color_discrete_map={"good": "blue", "excellent": "green", "fair": "orange"})
    fig.update_layout(title='Grafico de condición del auto vs el Kilometraje',
                      xaxis_title='Condición', yaxis_title='Kilometraje')

    st.plotly_chart(fig, use_container_width=True)
