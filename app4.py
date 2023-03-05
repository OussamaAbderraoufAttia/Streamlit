#In this app we are going to see how to use the funcitons integrated in the streamlit package to create a simple app
#We are going to use the following functions:

#importing the necessary packages
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('GDG Qaada Data Science Meetup')
st.subheader("Streamlit Qaada!")
st.markdown("This app allows you to understad how to use streamlit to create a simple app and how to visualise data in a simple way and you don't have to have a lot of knowledge!")

#Create a normal distribution using numpy
data = np.random.standard_normal(size=1000)
#Linear plots:
st.line_chart(data)

#Create a dataframe
df = pd.DataFrame(
                np.random.rand(10, 4),
                columns= ["NO2","C2H5CH","VOC","CO"])
df['date'] =  pd.date_range("2023-01-01", periods=10, freq="m")
df_melted = pd.melt(df,id_vars=['date'],var_name='parameter', value_name='value')
c = alt.Chart(df_melted, title='measure of different elements over time').mark_line().encode(
     x='date', y='value', color='parameter')

st.altair_chart(c, use_container_width=True)


#read the csv file
#this csv file contains the coordinates of the cities in the US
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')
#Create a map
st.map(df)
