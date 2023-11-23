import streamlit as st
import pandas as pd
import openpyxl


data = pd.read_excel('fashionsales.xlsx', engine='openpyxl')

# Configuración del título y la descripción
st.title('Datos de Ventas de ropa en Australia')
st.write('Este es un dashboard simple para analizar datos de ventas para la ayuda de toma de decisiones.')

# Filtrar los datos por mes
selected_month = st.selectbox('Seleccionar mes:', data['Month'].unique())
filtered_data = data[data['Month'] == selected_month]

# Mostrar los datos filtrados
st.write(f'Datos para el mes seleccionado: {selected_month}')
st.write(filtered_data)

# Gráfico de barras para las ventas por categoría
st.subheader('Ventas por Categoría')
category_sales = filtered_data.groupby('Category')['Sales'].sum()
st.bar_chart(category_sales)

# Gráfico de barras para las ventas por estado
st.subheader('Ventas por Estado')
state_sales = filtered_data.groupby('State')['Sales'].sum()
st.bar_chart(state_sales)

# Gráfico de barras para las ventas por manager
st.subheader('Ventas por Manager')
manager_sales = filtered_data.groupby('Manager')['Sales'].sum()
st.bar_chart(manager_sales)

# Gráfico de líneas para las ventas a lo largo del tiempo
st.subheader('Ventas a lo largo del tiempo')
time_series_data = data.groupby('Month')['Sales'].sum()
st.line_chart(time_series_data)

# Tabla de resumen
st.subheader('Resumen de Ventas')
summary = data.groupby(['Month', 'Category'])['Sales'].sum().unstack()
st.dataframe(summary)





