import streamlit as st
import streamlit.components.v1 as stc

import pandas as pd
import neattext.functions as nfx

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import altair as alt

def load_bible(data):
    df = pd.read_csv(data)
    return df


def main():
    st.title("Stream Bible")
    menu = ["Home", "MultiVerse", "About"]

    df = load_bible("data/KJV_Bible.csv")

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Single Verse Search")

        book_list = df['book'].unique().tolist()
        book_name = st.sidebar.selectbox("Book", book_list)

        chapter = st.sidebar.number_input("Chapter", 1)
        verse = st.sidebar.number_input("verse", 1)

        bible_df = df[df['book'] == book_name]
        st.dataframe(bible_df)

    
    elif choice == "MultiVerse":
        st.subheader("Multi Verse Analysis")
    else:
        st.subheader("About Bible App")


if __name__ == '__main__':
    main()