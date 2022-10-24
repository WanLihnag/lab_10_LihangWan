import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')
st.title('California Housing Data (1990) by Lihang Wan')

df = pd.read_csv('housing.csv')

value_filter = st.slider('Minimal Median House Value:', 0, 500001, 200000)

location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),
     df.ocean_proximity.unique())

form = st.sidebar.radio("median_income",('Low','Medium','High'))
df = df[df.median_house_value >= value_filter]
df = df[df.ocean_proximity.isin(location_filter)]

if form =='Low':
    df = df[df.median_income <= 2.5]
elif form == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
else :
    df = df[df.median_income >= 4.5]



st.subheader('See more filters in the sidebar:')
st.map(df)

st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(13,8))
val = df.median_house_value.hist(bins=30)
st.pyplot(fig)
