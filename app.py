import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Analisis de Datos de Vehiculos Usados')
st.subheader('Explora las caracteristicas de los autos en Estados Unidos')
st.write('Esta app permite visualizar histogramas y graficos de dispersion.\nVisualiza segun:')
# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')
# Crear casillas de verificacion.
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

# Si el usuario marca la casilla de histograma
if build_histogram:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Si el usuario marca la casilla de dispersión
if build_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Relación entre odómetro y precio")
    st.plotly_chart(fig, use_container_width=True)
