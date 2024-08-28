import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Configuración del slider
angle = st.slider('Ángulo', min_value=0.0, max_value=90.0, value=0.0,step=0.1)

# Calcular seno y coseno
radianes = np.radians(angle)
sin_value = np.sin(radianes)*2
cos_value = np.cos(radianes)*2
r2=np.max(cos_value)*0.5
# Crear el círculo
theta = np.linspace(0,  2*np.pi, 100)
x_circle = np.cos(theta)*2
y_circle = np.sin(theta)*2

theta2 = np.linspace(0,  radianes, 100)
x_circle2=np.cos(theta2)*r2 
y_circle2=np.sin(theta2)*r2

# Crear el triángulo (vértices del triángulo rectángulo)
x_triangle = [0, cos_value, cos_value,0]
y_triangle = [0, 0, sin_value, 0]
# Crear la figura
fig = go.Figure()

# Añadir el círculo
fig.add_trace(go.Scatter(x=x_circle, y=y_circle, mode='lines', name='Círculo'))


# Añadir el triángulo
fig.add_trace(go.Scatter(x=x_triangle, y=y_triangle, mode='lines+markers', name='Triángulo', fill='toself'))


#############ANOTACIONES DEL LADO DERECHO
fig.add_annotation(x=3.5, y=0.3, text=f"cos(θ) = {cos_value*0.5:.5f}", showarrow=False,
                   font=dict(size=25, color="darkblue"))
fig.add_annotation(x=3.5, y=-0.3, text=f"sin(θ) = {sin_value*.5:.5f}", showarrow=False,
                   font=dict(size=25, color="darkgreen"))
fig.add_annotation(x=3., y=.8, text=f"θ={angle}°", showarrow=False,
                   font=dict(size=25, color="darkred"))

#AGREGO EL ANGULO
fig.add_trace(go.Scatter(x=x_circle2, y=y_circle2, mode='lines', name='θ'))

fig.add_annotation(x=0.5*r2, y=.1, text=f"θ", showarrow=False,
                   font=dict(size=18, color="darkred"))




# Configurar los ejes y el aspecto del gráfico
fig.update_layout(
    xaxis=dict(scaleanchor="y", scaleratio=1),
    yaxis=dict(scaleanchor="x", scaleratio=1),
    xaxis_range=[-2.25, 2.25],
    yaxis_range=[-2.25, 2.25],
    title=""
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)


#####################
# Título de la aplicación
st.title("Gráfica de Seno y Coseno ")

# Slider para seleccionar el ángulo en grados
angle_deg = st.slider("Selecciona el ángulo en grados", min_value=0.0, max_value=360.0, value=0.0,step=0.1)

# Convertir el ángulo a radianes
angle_rad = np.deg2rad(angle_deg)

# Generar valores de ángulo para graficar
x = np.linspace(0, 2 * np.pi, 360)

# Calcular el seno y coseno para cada valor de x
y_sin = np.sin(x)
y_cos = np.cos(x)

# Crear la figura con Plotly
fig = go.Figure()

# Agregar las trazas de seno y coseno
fig.add_trace(go.Scatter(x=x, y=y_sin, mode='lines', name='Seno'))
fig.add_trace(go.Scatter(x=x, y=y_cos, mode='lines', name='Coseno'))

# Marcar el ángulo seleccionado en la gráfica
fig.add_trace(go.Scatter(
    x=[angle_rad],
    y=[np.sin(angle_rad)],
    mode='markers',
    name=f'Seno({angle_deg}°)={np.sin(angle_rad):.3f}',
    marker=dict(color='red', size=10)
))
fig.add_trace(go.Scatter(
    x=[angle_rad],
    y=[np.cos(angle_rad)],
    mode='markers',
    name=f'Coseno({angle_deg}°)={np.cos(angle_rad):.3f}',
    marker=dict(color='blue', size=10)
))

# Configurar los ejes
fig.update_layout(
    xaxis_title='Ángulo ',
    yaxis_title='Valor',
    title= f'θ={angle_deg}°',
    showlegend=True
)

# Mostrar la gráfica en Streamlit
st.plotly_chart(fig)