#import the necessary modules
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

#Read the csv file
df = pd.read_csv('newyork.csv')

#create teh