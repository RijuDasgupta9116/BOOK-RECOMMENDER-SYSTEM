# import streamlit as st
# import pickle
#
# st.header('Book-Recomender-System')
#
# books = pickle.load(open('model/books_list.pkl','rb'))
# similarity = pickle.load(open('model/similarity.pkl','rb'))
#
# books_list = books['title'].values
#
# selected_books = st.selectbox(
#     "Type or select a book from the drop-down",
#     books_list
# )
#
# def recommend(movie):
#     index = books[books['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
#     col1, col2, col3, col4, col5 = st.beta_columns(5)
#
#     with col1:
#         st.text(books.iloc[distances[1][0]].title)
#         st.image(books.iloc[distances[1][0]].thumbnail)
#     with col2:
#         st.text(books.iloc[distances[2][0]].title)
#         st.image(books.iloc[distances[2][0]].thumbnail)
#     with col3:
#         st.text(books.iloc[distances[3][0]].title)
#         st.image(books.iloc[distances[3][0]].thumbnail)
#     with col4:
#         st.text(books.iloc[distances[4][0]].title)
#         st.image(books.iloc[distances[4][0]].thumbnail)
#     with col5:
#         st.text(books.iloc[distances[5][0]].title)
#         st.image(books.iloc[distances[5][0]].thumbnail)
#
#
#
# if st.button('Show Recommendation'):
#     recommend(selected_books)
#
#

import pickle
import streamlit as st
import pandas as pd

def recommend(book):
    index=books_list[books_list['title']==book].index[0]
    distances=similarity[index]
    books=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_books=[]
    recommended_books_poster=[]
    for i in books:
        recommended_books.append(books_list.iloc[i[0]].title)
        recommended_books_poster.append(books_list.iloc[i[0]].thumbnail)
    return recommended_books,recommended_books_poster



st.header('BOOK RECOMMENDER SYSTEM')
books_dict=pickle.load(open('model/books_list_dict.pkl','rb'))
books_list=pd.DataFrame(books_dict)

similarity=pickle.load(open('model/similarity.pkl','rb'))
selected_book_name=st.selectbox(
"Type or select a book from the dropdown",
books_list['title'].values)

if st.button('Recommend'):
    names,posters=recommend(selected_book_name)
    col1,col2,col3,col4,col5=st.beta_columns(5)
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