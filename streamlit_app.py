import streamlit as st
import pandas as pd
import openpyxl
import plotly.express as px

# Cargar los datos
datos = pd.read_excel('fashionsales.xlsx', engine='openpyxl')

# Icono y título
icono_url = 'icono.jpg'
st.image(icono_url, width=100)
st.title('Reporte de Ventas de Ropa y Accesorios')

# Descripción
st.write('Este es un panel de control para analizar datos de ventas y facilitar la toma de decisiones.')

# Gráfico de líneas para las ventas a lo largo del tiempo
st.subheader('Ventas a lo largo del tiempo')
datos['Month'] = pd.to_datetime(datos['Month'], format='%d/%m/%Y', errors='coerce').dt.strftime('%Y-%m')
serie_temporal_ventas = datos.groupby('Month')['Sales'].sum()
st.line_chart(serie_temporal_ventas)

# Filtrar los datos por mes
mes_seleccionado = st.selectbox('Seleccionar mes:', datos['Month'].unique())
datos_filtrados = datos[datos['Month'] == mes_seleccionado]

# Mostrar los datos filtrados
st.write(f'Datos para el mes seleccionado: {mes_seleccionado}')
st.write(datos_filtrados)

st.markdown('<br>', unsafe_allow_html=True) 

# Gráfico de barras para las ventas por categoría
st.subheader('Ventas por Categoría')
ventas_por_categoria = datos_filtrados.groupby('Category')['Sales'].sum()
st.bar_chart(ventas_por_categoria)

# Gráfico de Torta para la Distribución de Categorías
st.subheader('Distribución de Categorías')
distribucion_categorias = datos['Category'].value_counts()
figura_torta = px.pie(distribucion_categorias, labels=distribucion_categorias.index,
                     values=distribucion_categorias.values, title='Distribución de Categorías',
                     hole=0.3, names=distribucion_categorias.index)
st.plotly_chart(figura_torta)

st.markdown('<br>', unsafe_allow_html=True) 

# Gráfico de barras para las ventas por estado
st.subheader('Ventas por Estado')
ventas_por_estado = datos_filtrados.groupby('State')['Sales'].sum()
st.bar_chart(ventas_por_estado)

st.markdown('<br>', unsafe_allow_html=True) 

# Gráfico de barras para las ventas por manager
st.subheader('Ventas por Gerente')
ventas_por_gerente = datos_filtrados.groupby('Manager')['Sales'].sum()
st.bar_chart(ventas_por_gerente)
