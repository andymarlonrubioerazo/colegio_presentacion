import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random


st.latex(r'\sin^2(\theta) + \cos^2(\theta) = 1')
    
w = st.slider("Frecuencia", min_value=1.0, max_value=5.0,step=0.1)

# Gráfico interactivo usando Plotly
t = np.linspace(0, 4*np.pi, 400)

y_sin = np.sin(w*t)
y_cos = np.cos(w*t) 

y_sin_sq = np.sin(w*t) ** 2
y_cos_sq = np.cos(w*t) ** 2
y_sum = y_sin_sq + y_cos_sq


fig1 = go.Figure()

fig1.add_trace(go.Scatter(x=t, y=y_sin, mode='lines', name='sin²(θ)'))
fig1.add_trace(go.Scatter(x=t, y=y_cos, mode='lines', name='cos²(θ)'))


fig1.update_layout(title='Seno y Coseno',
                xaxis_title='Ángulo (θ)',
                yaxis_title='Valor',
                yaxis=dict(range=[-1.1 ,1.1]),
                legend_title='Funciones',
                width=600,  # Ancho del gráfico
                height=300)

st.plotly_chart(fig1)

fig = go.Figure()


fig.add_trace(go.Scatter(x=t, y=y_sin_sq, mode='lines', name='sin²(θ)'))
fig.add_trace(go.Scatter(x=t, y=y_cos_sq, mode='lines', name='cos²(θ)'))
fig.add_trace(go.Scatter(x=t, y=y_sum, mode='lines', name='sin²(θ) + cos²(θ)', 
                        line=dict(color='firebrick', width=4, dash='dash')))

fig.update_layout(title='Suma de los Cuadrados del Seno y el Coseno',
                xaxis_title='Ángulo (θ)',
                yaxis_title='Valor',
                yaxis=dict(range=[-.1 ,1.1]),
                legend_title='Funciones',
                width=600,  # Ancho del gráfico
                height=300)

st.plotly_chart(fig)

# Agregar más identidades de forma similar

# Ejemplos y ejercicios
st.subheader("Ejercicio 1: Selecciona el valor correcto")
st.write("Selecciona la opción correcta que satisface la identidad.")

# Generación de un valor aleatorio para x
x_random =random.choice([30, 45, 60, 90, 120, 150, 180])
st.write(f"Para x = {x_random} grados:")

# Cálculo de la identidad
correct_result = 1

# Opciones para seleccionar
options = [correct_result, correct_result + random.uniform(-0.5, 0.5), correct_result + random.uniform(-1, 1)]
random.shuffle(options)

# Selección del usuario
x0 = st.selectbox("¿Cuál es el resultado correcto de $\sin^2(x) + \cos^2(x)$ ?", 
                            options,placeholder="Escoja una opción",key="x0")


# Verificación de la respuesta
if st.button("Confirmar") :
    if 1==x0:

        st.success("¡Correcto! Seleccionaste la opción correcta.")
    else:
        st.error("Respuesta incorrecta. Intenta de nuevo.")
        # st.error("Recuerda, sin importar el valor de x, siempre $\sin^2(x) + \cos^2(x)$ debe ser igual a 1.")
        # Más ejercicios o información adicional
