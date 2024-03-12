# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:24:57 2024

@author: cex
"""

import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import re
import seaborn as sns 
from matplotlib.colors import ListedColormap


locations = pd.read_csv("C:\\Users\\cex\\Documents\\top 50 Bars\\locations.txt")
top_bars_2024_og = pd.read_csv("C:\\Users\\cex\\Documents\\top 50 Bars\\top_bars.txt")
top_bars_2024 = top_bars_2024_og.copy()

top_bars_2022_og = pd.read_csv("C:\\Users\\cex\\Documents\\top 50 Bars\\top_bars_2022.txt")
top_bars_2023_og = pd.read_csv("C:\\Users\\cex\\Documents\\top 50 Bars\\top_bars_2023.txt")
top_bars_2024_og = pd.read_csv("C:\\Users\\cex\\Documents\\top 50 Bars\\top_bars.txt")

#Copy into new variables 
top_bars_2022 = top_bars_2022_og.copy()
top_bars_2023 = top_bars_2023_og.copy()
top_bars_2024 = top_bars_2024_og.copy()

#Putting rank into the 2022
top_bars_2022['Rank'] = top_bars_2022.index+1

#Removing leading spaces on 2022 
top_bars_2022['Location'] = top_bars_2022['Location'].str.strip().str.strip()

#Reorder columns
top_bars_2022 = top_bars_2022[['Rank', 'Bar', 'Location']]

#Reorder our location data 
locations = locations[['Location', 'Latitude', 'Longitude']]

#Turn the rank from 1st to 1. 
top_bars_2024['Rank'] = top_bars_2024['Rank'].apply(lambda x: re.findall(r'\d+', x)[0]).astype(int)


#Create a binary column for London venues 
london = ['Bethnal Green', 'Soho', 'Kensington', 'Shoreditch', 'Mayfair', 'Dalston', 'Hackney',
          'Newington Green', 'Covent Garden','Crouch End', 'Spitalfields','Holborn',
       'Islington', 'Fitzrovia','South Bank', 'Chinatown',
 'Hoxton', 'Liverpool St', 'Oxford Circus', 'South Kensington', 'Chinatown',
 'Haggerston', 'Marylebone',  'Notting Hill',  'Smithfield Market', 'South Kensington']
scotland = ['Auchterarder', 'Edinburgh', 'Glasgow']
rest_of_england = ['Manchester', 'Birmingham', 'Leeds', 'Bristol', 
       'Bath', 'Sheffield', 'Bournemouth', 'Brighton', 'Liverpool', 'Nottingham', 'Brighton', 'Liverpool', 'Newcastle upon Tyne' ]
wales = ['Cardiff']

dfs = [top_bars_2022, top_bars_2023, top_bars_2024] 

#Adding the boolean in London column 
for df in dfs:
    df['in_london'] = df['Location'].isin(london).astype('int').astype('bool')

#Turning rank into an integer 
for df in dfs:
    df['Rank'] = df['Rank'].astype('int')

#Fixing 🔶🟥🔵 and Tayēr + Elementary
top_bars_2022.loc[10, 'Bar'] = 'a Bar with shapes for a name'
top_bars_2023.loc[8, 'Bar'] = 'a Bar with shapes for a name'
top_bars_2024.loc[9, 'Bar'] = 'Tayēr + Elementary'
top_bars_2024.loc[7, 'Bar'] = 'Amaro'

#Cleaning bar names 
for df in dfs:
    df['Bar'] = df['Bar'].str.strip('.').str.title().str.replace("'S", "'s")
  
##Checking Tayer 
#top_bars_2023.loc[2,'Bar'] == top_bars_2024.loc[9, 'Bar']

st.title('The Mysterious and Wonderful Cocktail bar recommendation machine')
st.subheader('Everything is not as it seems')



st.write('Good afternoon and welcome to the interactive, mysterious and wonderful Cocktail Bar recommendation machine. We will find the very best bar for your location and state of time travel.')
st.write("Are you living in the present or the past? You may think you know what year you're in but maybe you're wrong...")

st.image("C:\\Users\\cex\\OneDrive\\Pictures\\Saved Pictures\\cocktail_rec.jpg")

st.write("Take a look around, but don't trust those pesky newspapers, they're always trying to decieve us")

st.subheader('Have you time travelled unexpectedly?')
year = st.radio("Go on... Take a guess, what year are you in?", [2022, 2023, 2024])

if year == 2022:
    data = top_bars_2022
elif year == 2023: 
    data = top_bars_2023
elif year == 2024:
    data = top_bars_2024
else:
    pass

st.subheader('Do you know you current location? Or have you astral projected to somewhere unknown?')
st.write("Now let's do the same with where you are. Don't look at the road signs, or google maps. Use your eyes, really use them.")
st.write("Go on... Take a guess... Where are you, we'll start simple and narrow it down.")
LDNYN = st.radio('Are you in London?', ['Yes', 'No'])


if LDNYN == 'Yes':
    data = data[data['in_london'] == True]
else:
    data = data[data['in_london'] == False]

loc_ops = data.Location.unique()

location = st.selectbox('Well then where are ya?', loc_ops)

st.write('Then here are some bar reccomendations from The UKs top 50 Bars')

st.write(top_bars_2023[top_bars_2023['Location'] == location][['Bar']])




