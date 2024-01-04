# %%
import os.path
import os
import pandas as pd
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space 

# %%
raw_quran = pd.read_csv('./Arabic-Original.csv/Arabic-Original.csv', header=None)
surah_names = pd.read_csv('./Arabic-Original.csv/surahList.csv', header=None)

# Directory path
directory = './Surah'

# Initialize an empty dictionary to store the DataFrames
dataframes = {}

# Iterate over the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Read the file into a DataFrame
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath)
        
        # Store the DataFrame in the dictionary with the filename as the key
        dataframes[filename] = df


# %%
with st.sidebar:
    st.title('Quran Search -- UNFINISHED')
    st.subheader('Select Surah')
selected_surahs = st.sidebar.selectbox('Surah', surah_names[1])+ '.csv'


variable = pd.DataFrame()
if st.button('Search'):
    if selected_surahs:
        for df in dataframes.keys():
            if df == selected_surahs:
                variable = dataframes[df]
                # for index, row in dataframes[df].iterrows():
                #     st.checkbox(row.values[0])
    else:
        st.write('Please select at least one Surah')
checkbox_states = []
def createCheckbox(variable):
    for index, row in variable.iterrows():
        checkbox_states.append(st.write(row.values[0]))
    return checkbox_states
# for index, row in variable.iterrows():
    # st.checkbox(row.values[0])
createCheckbox(variable)
# st.checkbox('la knti rajl ghbr')

