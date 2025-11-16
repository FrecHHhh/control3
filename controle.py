import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("database_titanic.csv")

st.write("control")

with st.sidebar:
    st.write("barra")

div = st.slider('numero de bins:', 0, 10, 2)

st.write("Bins=", div)

fig, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].hist(df["Age"], bins=div)
ax[0].set_xlabel("Edad")
ax[0].set_ylabel("Frecuencia")
ax[0].set_title("Histograma de edades")

df_male  = df[df["Sex"] == "male"]
cant_male = len(df_male)

df_female = df[df["Sex"] == "female"]
cant_female = len(df_female)

ax[1].bar(["Masculino", "femenino"], [cant_male, cant_female], color = "red")
ax[1].set_xlabel("Sexo")
ax[1].set_ylabel("Cantidad")
ax[1].set_title('Distribucion de hombres y mujeres')

st.pyplot(fig)

st.write("aaaa")
st.table(df.head())