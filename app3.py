import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.random.standard_normal(size=1000) #create a normal distribution using numpy
data = pd.DataFrame(data, columns=['x']) #create a dataframe with the data
st.dataframe(data)

fig, ax = plt.subplots()
#Ask the user to input the number of bins
nb_bins = st.number_input('Number of bins', min_value=1, max_value=100, value=20)


#Ask the user to input the title of the histogram
graph_title  = st.text_input('Title', 'Histogram')

#Ask the user to input the color of the histogram
graph_color = st.color_picker('Pick a color', '#00f900')

ax.set_title(graph_title)
ax.hist(data['x'], nb_bins, color= graph_color)

st.pyplot(fig)