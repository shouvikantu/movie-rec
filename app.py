import pickle
import pandas as pd
import streamlit as st


movies_dict = pickle.load(open('Movies_dict.pkl','rb'))
movie_list = pd.DataFrame(movies_dict)
st.title('Movie Recommending System')

option = st.selectbox("Choose a Movie.", movie_list['title'].values)