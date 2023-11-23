import streamlit as st
import pandas as pd
import openpyxl

# Cargar los datos
data = pd.read_excel('fashionsales.xlsx', engine='openpyxl')

# Configuración del título y la descripción
st.title('Datos de Ventas de Ropa en Australia')
st.write('Este es un dashboard simple para analizar datos de ventas para la ayuda de toma de decisiones.')


# Estadísticas descriptivas
st.subheader('Estadísticas de Ventas')
st.write(filtered_data['Sales'].describe())

# Filtrar los datos por mes
selected_month = st.selectbox('Seleccionar mes:', data['Month'].dt.to_period('M').unique())
filtered_data = data[data['Month'].dt.to_period('M') == selected_month]

# Gráfico de barras para las ventas por categoría
st.subheader(f'Ventas por Categoría para {selected_month}')
category_sales = filtered_data.groupby('Category')['Sales'].sum()
st.bar_chart(category_sales)


# Mostrar los datos filtrados
st.subheader(f'Datos para {selected_month}')
st.write(filtered_data)

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
time_series_data = data.groupby(data['Month'].dt.to_period('M'))['Sales'].sum()
st.line_chart(time_series_data)

# Tabla de resumen
st.subheader('Resumen de Ventas')
summary = data.groupby([data['Month'].dt.to_period('M'), 'Category'])['Sales'].sum().unstack()
st.dataframe(summary)
