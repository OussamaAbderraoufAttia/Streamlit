import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = np.random.standard_normal(size=1000) #create a normal distribution using numpy 
data = pd.DataFrame(data, columns=['x']) #create a dataframe with the data

#st.write(data)
st.dataframe(data)
st.line_chart(data)

#Here now we are going to plot a histogram but it can't be showed
#because we are not using the st.pyplot() function
plt.hist(data['x'], bins=20)
plt.show()
st.pyplot() #This is the function that shows the plot
#But we will get a warning because it expects arguments which are not given
fig, ax = plt.subplots() #This is the way to get rid of the warning
ax.hist(data['x'], bins=20)
st.pyplot(fig)