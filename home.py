import calendar

import streamlit as st
import pandas as pd
import plotly.express as px


st.header("Leonardo Pacheco Rosas")

dfCafeteria = pd.read_csv("datos/CafeDatosFinalesNov2024.csv")


dfCafeteria.drop(columns=["Unnamed: 0", "index", "temp"], inplace=True)

dfCafeteria["fecha"]= pd.to_datetime(dfCafeteria["fecha"], format="%Y-%m-%d")

dfCafeteria["fecha y hora"]= pd.to_datetime(dfCafeteria["fecha y hora"], format="%Y-%m-%d %H:%M:%S.%f")
nombresDias = list(calendar.day_name)

st.dataframe(dfCafeteria)

with st.sidebar:
    diaSemana = st.selectbox(
	    "elige un dia de la semana",
	    ("Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday")
	)

st.write("Dia elegido:", diaSemana)

tituloFiltro = "seleccionando solamente el dia:" + diaSemana
st.header(tituloFiltro)

dfFiltrado = dfCafeteria[dfCafeteria["diaDeLaSemana"]==diaSemana]

st.dataframe(dfFiltrado)

contadores = dfCafeteria["diaDeLaSemana"].value_counts()

dfContadores = contadores.rename_axis("Dia de la semana").reset_index(name="contador")

fig = px.bar(dfContadores, x="Dia de la semana", y="contador", title="Numero de visitas por dia")

st.plotly_chart(fig, use_container_width=True)


print(dfCafeteria.dtypes)
df2018 = dfCafeteria[dfCafeteria["fecha"].dt.year == 2018]

st.write("Durante el 2018 cual fue el año con mas visitas")
#1.Filtrar nuestros datos mostrando unicamente 2018
#2. Agrupar por mes
grupos = df2018.groupby(pd.Grouper(key="fecha", axis=0,freq="M")).count()

st.dataframe(grupos)
grupos.reset_index(inplace=True)
st.dataframe(grupos)
fig = px.bar(grupos, x= "fecha", y="fecha y hora", title="Numero de visitas por mes en el 2018")
st.plotly_chart(fig, use_container_width=True)