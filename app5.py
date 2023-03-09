#import the necessary modules
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

#Add a title
st.title('GDG Qaada Data Science Meetup')

#Add a subheader
st.subheader('Streamlit Qaada!')

#Add a description
st.write('This app allows you to understad how to use streamlit to create a simple app and how to visualise data in a simple way and you don''t have to have a lot of knowledge!')

#Read the csv file
df = pd.read_csv('Automobile_data.csv')

#explore the data
st.dataframe(df)

#show the columns
st.write(df.columns)

#show the shape of the data
st.write(df.shape)

#show the data types
st.write(df.dtypes)

#show the statistics of the data
st.write(df.describe())

#show the unique values of the data
st.write(df['make'].unique())

#visualise the data
#Create a histogram
st.subheader('Histogram')
#Ask the user to input the number of bins
nb_bins = st.number_input('Number of bins', min_value=1, max_value=100, value=20)
#Ask the user to input the title of the histogram
graph_title  = st.text_input('Title', 'Histogram')
#Ask the user to input the color of the histogram
graph_color = st.color_picker('Pick a color', '#00f900')

#Create the histogram
fig, ax = plt.subplots()
ax.set_title(graph_title)
ax.hist(df['price'], nb_bins, color= graph_color)
st.pyplot(fig)

#Create a bar chart
st.subheader('Bar chart')




