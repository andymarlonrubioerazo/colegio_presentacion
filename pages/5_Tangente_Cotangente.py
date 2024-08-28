import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random

st.subheader("Relación de la tangente y secante")
st.latex(r'1+\tan^2(\theta)  = \sec^2(\theta)')

w = st.slider("Ángulo "+r"($\theta$)", min_value=1.0, max_value=5.0,step=0.1)

# Gráfico interactivo usando Plotly
t = np.linspace(0, 4*np.pi, 400)

y_tan = np.tan(w*t)
y_sec = 1./np.cos(w*t) 

y_tan_sq =y_tan**2.0 
y_sec_seq = y_sec**2.0
y_sum = y_tan_sq+1.0
x_1=np.ones(len(t))

fig1 = go.Figure()

fig1.add_trace(go.Scatter(x=t, y=y_tan, mode='lines', name='tan(θ)'))
fig1.add_trace(go.Scatter(x=t, y=y_sec, mode='lines', name='sec(θ)'))
fig1.add_trace(go.Scatter(x=t, y=x_1, mode='lines', name='1'))

fig1.update_layout(title='Tangente y Secante',
                xaxis_title='Ángulo (θ)',
                yaxis_title='Valor',
                # yaxis=dict(range=[-1.1 ,1.1]),
                legend_title='Funciones',
                width=600,  # Ancho del gráfico
                height=300)

st.plotly_chart(fig1)

fig = go.Figure()


fig.add_trace(go.Scatter(x=t, y=y_tan_sq, mode='lines', name='tan²(θ)'))
fig.add_trace(go.Scatter(x=t, y=x_1, mode='lines', name='1'))
fig.add_trace(go.Scatter(x=t, y=y_sum, mode='lines', name='sec²(θ)=1 + tan²(θ)', 
                        line=dict(color='firebrick', width=4, dash='dash')))

fig.update_layout(title='Cuadrado de Secante',
                xaxis_title='Ángulo (θ)',
                yaxis_title='Valor',
                # yaxis=dict(range=[-.1 ,1.1]),
                legend_title='Funciones',
                width=600,  # Ancho del gráfico
                height=300)

st.plotly_chart(fig)

st.subheader("Relación de la cotangente y cosecante")
st.latex(r'1+\cot^2(\theta)  = \csc^2(\theta)')

w1 = st.slider("Ángulo "+r"($\theta$)", min_value=1.0, max_value=5.0,step=0.1,key="w1")

# Gráfico interactivo usando Plotly
t = np.linspace(0, 4*np.pi, 400)

y_cot = 1/np.tan(w1*t)
y_csc = 1./np.sin(w1*t) 

y_cot_sq =y_cot**2.0 
y_csc_seq = y_csc**2.0
y_sum = y_cot_sq+1.0
x_1=np.ones(len(t))

fig2 = go.Figure()

fig2.add_trace(go.Scatter(x=t, y=y_cot, mode='lines', name='cot(θ)'))
fig2.add_trace(go.Scatter(x=t, y=y_csc, mode='lines', name='csc(θ)'))
fig2.add_trace(go.Scatter(x=t, y=x_1, mode='lines', name='1'))



fig2.update_layout(title='Tangente y Secante',
                xaxis_title='Ángulo (θ)',
                yaxis_title='Valor',
                # yaxis=dict(range=[-1.1 ,1.1]),
                legend_title='Funciones',
                width=600,  # Ancho del gráfico
                height=300)

st.plotly_chart(fig2)

fig3 = go.Figure()


fig3.add_trace(go.Scatter(x=t, y=y_cot_sq, mode='lines', name='cot²(θ)'))
fig3.add_trace(go.Scatter(x=t, y=x_1, mode='lines', name='1'))
fig3.add_trace(go.Scatter(x=t, y=y_sum, mode='lines', name='csc²(θ)=1 + cot²(θ)', 
                        line=dict(color='firebrick', width=4, dash='dash')))

fig3.update_layout(title='Cuadrado del Cosecante',
                xaxis_title='Ángulo (θ)',
                yaxis_title='Valor',
                # yaxis=dict(range=[-.1 ,1.1]),
                legend_title='Funciones',
                width=600,  # Ancho del gráfico
                height=300)

st.plotly_chart(fig3)





options=["Tan(x)", "Cot(x)","Sin(x)","Cos(x)","Csc(x)","Sec(x)","1"]

st.header("Se debe ingresar las opciones para cada relacion")
st.subheader("Relación de la Tangente cuadrada")


col1,col2, col3=st.columns(3)
with col1: x0=st.selectbox("Op1",options=options,placeholder="Seleccione una opción",index=None)
with col2: x1=st.selectbox("Op2",options=options,placeholder="Seleccione una opción",index=None)
with col3: x2=st.selectbox("Op3",options=options,placeholder="Seleccione una opción",index=None)

y1=f"{x0}+{x1}²={x2}²"
y2=f"{x0}²+{x1}={x2}²"
if x0 is not None or x1 is not None or x2 is not None: 
    st.subheader(f"{x0}²+{x1}²={x2}²")

if y1=="1+Tan(x)²=Sec(x)²" or y2=="Tan(x)²+1=Sec(x)²": 
    st.success("Felicidades",icon="✅")
else: st.error("Ingrese los valores correcto")

st.subheader("Relación de la Cotangente cuadrada")

col4,col5, col6=st.columns(3)
with col4: x3=st.selectbox("Op4",options=options,placeholder="Seleccione una opción",index=None)
with col5: x4=st.selectbox("Op5",options=options,placeholder="Seleccione una opción",index=None)
with col6: x5=st.selectbox("Op6",options=options,placeholder="Seleccione una opción",index=None)

y3=f"{x3}+{x4}²={x5}²"
y4=f"{x3}²+{x4}={x5}²"
if x3 is not None or x4 is not None or x5 is not None: 
    st.subheader(f"{x3}²+{x4}²={x5}²")

if y3=="1+Cot(x)²=Csc(x)²" or y4=="Cot(x)²+1=Csc(x)²": 
    st.success("Felicidades",icon="✅")
else: st.error("Ingrese los valores correcto")