import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random

st.subheader("Identidades Trigonométricas: :triangular_ruler:")
col1, col2=st.columns(2)
with col1: 
    st.latex(r'\sin(\theta) = \frac{\text{Cateto Opuesto}}{\text{Hipotenusa}}')
    st.latex(r'\cos(\theta) = \frac{\text{Cateto Adyacente}}{\text{Hipotenusa}}')
    st.latex(r'\tan(\theta) = \frac{\text{Cateto Opuesto}}{\text{Cateto Adyacente}}')
    st.latex(r'\sec(\theta) = \frac{\text{Hipotenusa}}{\text{Cateto Adyacente}}')
    st.latex(r'\csc(\theta) = \frac{\text{Hipotenusa}}{\text{Cateto Opuesto}}')
    st.latex(r'\cot(\theta) = \frac{\text{Cateto Adyacente}}{\text{Cateto Opuesto}}')

with col2: st.image("triangulo2.png")

st.subheader("Identidades Recíprocas:")

col7,col8, col9=st.columns(3)
col10,col11, col12=st.columns(3)

with col7: st.latex(r'\sin(\theta) = \frac{1}{\csc(\theta)}')
with col8: st.latex(r'\cos(\theta) = \frac{1}{\sec(\theta)}') 
with col9: st.latex(r'\tan(\theta) = \frac{1}{\cot(\theta)}') 
with col10: st.latex(r'\csc(\theta) = \frac{1}{\sin(\theta)}')
with col11: st.latex(r'\sec(\theta) = \frac{1}{\cos(\theta)}')
with col12: st.latex(r'\cot(\theta) = \frac{1}{\tan(\theta)}')