import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('vehicles_us.csv')
car_data_scatter = car_data.dropna(subset=['odometer', 'price'])
st.header('Análisis de vehículos usados')
st.write(car_data.head())

if 'chart_type' not in st.session_state:
    st.session_state.chart_type = None

show_histogram = st.button(
    'Mostrar histograma',
    key='histogram_button'
)
if show_histogram:
    st.session_state.chart_type = 'histogram'

show_scatter = st.button('Mostrar gráfico de dispersión', key='scatter_button')

if show_scatter:
    st.session_state.chart_type = 'scatter'

if st.session_state.chart_type == 'histogram':
    fig = px.histogram(car_data, x='price', nbins=50, title='Distribución de precios de vehiculos usados', labels={'price': 'Precio (USD)' })
    st.plotly_chart(fig, key='histogram_chart')

elif st.session_state.chart_type == 'scatter':
    fig = px.scatter(car_data_scatter, x='odometer', y='price', title='Relación entre kilometraje y precio', labels={'odometer': 'Kilometraje', 'price': 'Precio (USD)'})
    st.plotly_chart(fig, key='scatter_chart')

