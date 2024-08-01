# import streamlit as st 
# import pandas as pd 
# import numpy as np 
# import pickle
# import requests

# with open('movies.pkl', 'rb') as f:
#     movies = pickle.load(f)
# movies_list = movies['title'].values


# with open('similarity.pkl', 'rb') as f:
#     similarity = pickle.load(f)
# st.title('Movie Recommender System ')

# import streamlit as st 
# import pandas as pd 
# import numpy as np 
# import pickle
# import requests
# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=839e13741162dbbd7d8290a2a9dd7bea&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path


# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         # fetch poster from API
#         recommended_movies.append(movies.loc[i[0]].title)
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movies_posters

# st.header('Movie Recommender System')
# movies = pickle.load(open('movies.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# movie_list = movies['title'].values
# option = st.selectbox(
#     'How would you like to be contacted', 
#     movie_list)

    
# # To display this we'll use layout app 
# if st.button('Recommend'):
#     name, posters = recommend(option)
   
#     col1, col2, col3, col4, col5 = st.columns(3)
#     with col1:
#         st.header(name[0])
#         st.image(posters[0])
#     with col2:
#         st.header(name[1])
#         st.image(posters[1])
#     with col3:
#         st.header(name[2])
#         st.image(posters[2])
        
#     with col3:
#         st.header(name[3])
#         st.image(posters[3])
        
#     with col5:
#         st.header(name[4])
#         st.image(name[4])
        
        
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=839e13741162dbbd7d8290a2a9dd7bea&language=en-US"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
            return full_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image+Available"
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750?text=Error+Fetching+Image"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.loc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

st.header('Movie Recommender System')
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
option = st.selectbox(
    'Select a movie',
    movie_list
)

if st.button('Recommend'):
    names, posters = recommend(option)
   
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
