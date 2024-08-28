import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Configuración del slider





r0 = st.slider('Hipotenusa', min_value=1.0, max_value=10.0, value=5.0,step=0.02)

angle = st.slider('Ángulo', min_value=0.0, max_value=90.0, value=45.0,step=0.1)

# Calcular seno y coseno
radianes = np.radians(angle)
sin_value = np.sin(radianes)
cos_value = np.cos(radianes)




# Crear el triángulo (vértices del triángulo rectángulo)
x_triangle = [0, cos_value*r0, cos_value*r0,0]
y_triangle = [0, 0, sin_value*r0, 0]

r1=r0*cos_value
theta2 = np.linspace(0,  radianes, 100)
x_circle2=np.cos(theta2)*r1*0.5
y_circle2=np.sin(theta2)*r1*0.5

# Crear la figura

fig = go.Figure()

# Añadir el círculo

# Añadir el triángulo
fig.add_trace(go.Scatter(x=x_triangle, y=y_triangle, mode='lines+markers', name='Triángulo', fill='toself'))


#############ANOTACIONES DEL LADO DERECHO
fig.add_annotation(x=12, y=5., text=f"cos(θ) = ", showarrow=False,
                   font=dict(size=25, color="darkblue"))
fig.add_annotation(x=18, y=5., text=f" ={cos_value:.4f}", showarrow=False,
                   font=dict(size=25, color="darkblue"))
fig.add_annotation(x=15, y=5.35, text=f"_____", showarrow=False,
                   font=dict(size=25, color="darkblue"))
fig.add_annotation(x=15, y=5.35, text=f"{r0*cos_value:.3f}", showarrow=False,
                   font=dict(size=25, color="darkblue"))
fig.add_annotation(x=15, y=4.35, text=f"{r0}", showarrow=False,
                   font=dict(size=25, color="darkblue"))



fig.add_annotation(x=12, y=2, text=f"sin(θ) =", showarrow=False,
                   font=dict(size=25, color="darkgreen"))
fig.add_annotation(x=18, y=2, text=f" ={sin_value:.4f}", showarrow=False,
                   font=dict(size=25, color="darkgreen"))
fig.add_annotation(x=15, y=2.35, text="_____", showarrow=False,
                   font=dict(size=25, color="darkgreen"))
fig.add_annotation(x=15.0, y=2.4, text=f"{r0*sin_value:.3f}", showarrow=False,
                   font=dict(size=25, color="darkgreen"))
fig.add_annotation(x=15.0, y=1.4, text=f"{r0}", showarrow=False,
                   font=dict(size=25, color="darkgreen"))


fig.add_annotation(x=12, y=7, text=f"θ={angle}°", showarrow=False,
                   font=dict(size=25, color="darkred"))
fig.add_annotation(x=14, y=9, text=f"Hipotenusa={r0}", showarrow=False,
                   font=dict(size=25, color="darkred"))


#AGREGO EL ANGULO
fig.add_trace(go.Scatter(x=x_circle2, y=y_circle2, 
                         mode='lines', name='θ',line=dict(color='darkred')))

fig.add_annotation(x=cos_value*r0*0.25, y=sin_value*r1*0.2, text=f"θ", showarrow=False,
                   font=dict(size=18, color="darkred"))




# Configurar los ejes y el aspecto del gráfico
fig.update_layout(
    xaxis=dict(scaleanchor="y", scaleratio=1),
    yaxis=dict(scaleanchor="x", scaleratio=1),
    xaxis_range=[-1, 16],
    yaxis_range=[-1, 10],
    title=""
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)
st.image("triangulo.png", caption="Sunrise by the mountains")