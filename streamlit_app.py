import streamlit as st
import pandas as pd
import openpyxl

# Cargar los datos
data = pd.read_excel('fashionsales.xlsx', engine='openpyxl')

# Configuración del título y la descripción
st.title('Datos de Ventas de Ropa en Australia')
st.write('Este es un dashboard simple para analizar datos de ventas para la ayuda de toma de decisiones.')

# Selector de mes para el primer gráfico
selected_month_category = st.selectbox('Seleccionar mes para Ventas por Categoría:', data['Month'].dt.to_period('M').unique())
filtered_data_category = data[data['Month'].dt.to_period('M') == selected_month_category]

# Gráfico de barras para las ventas por categoría
st.subheader(f'Ventas por Categoría para {selected_month_category}')
category_sales = filtered_data_category.groupby('Category')['Sales'].sum()
st.bar_chart(category_sales)

# Selector de mes para el segundo gráfico
selected_month_state = st.selectbox('Seleccionar mes para Ventas por Estado:', data['Month'].dt.to_period('M').unique())
filtered_data_state = data[data['Month'].dt.to_period('M') == selected_month_state]

# Gráfico de barras para las ventas por estado
st.subheader(f'Ventas por Estado para {selected_month_state}')
state_sales = filtered_data_state.groupby('State')['Sales'].sum()
st.bar_chart(state_sales)

# Selector de mes para el tercer gráfico
selected_month_manager = st.selectbox('Seleccionar mes para Ventas por Manager:', data['Month'].dt.to_period('M').unique())
filtered_data_manager = data[data['Month'].dt.to_period('M') == selected_month_manager]

# Gráfico de barras para las ventas por manager
st.subheader(f'Ventas por Manager para {selected_month_manager}')
manager_sales = filtered_data_manager.groupby('Manager')['Sales'].sum()
st.bar_chart(manager_sales)

# Selector de mes para el cuarto gráfico
selected_month_time_series = st.selectbox('Seleccionar mes para Ventas a lo largo del tiempo:', data['Month'].dt.to_period('M').unique())
time_series_data = data.groupby(data['Month'].dt.to_period('M'))['Sales'].sum()
filtered_data_time_series = data[data['Month'].dt.to_period('M') == selected_month_time_series]

# Gráfico de líneas para las ventas a lo largo del tiempo
st.subheader(f'Ventas a lo largo del tiempo para {selected_month_time_series}')
st.line_chart(time_series_data)

# Selector de mes para la tabla de resumen
selected_month_summary = st.selectbox('Seleccionar mes para Resumen de Ventas:', data['Month'].dt.to_period('M').unique())
filtered_data_summary = data[data['Month'].dt.to_period('M') == selected_month_summary]

# Tabla de resumen
st.subheader(f'Resumen de Ventas para {selected_month_summary}')
summary = filtered_data_summary.groupby([data['Month'].dt.to_period('M'), 'Category'])['Sales'].sum().unstack()
st.dataframe(summary)
