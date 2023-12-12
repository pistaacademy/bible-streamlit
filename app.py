import streamlit as st
import streamlit.components.v1 as stc
import random

import pandas as pd
import neattext.functions as nfx

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import altair as alt

from utils import HTML_RANDOM_TEMPLATE, render_entities

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

        c1, c2 = st.columns([2,1])

        with c1:
            try:
                selected_passage = bible_df[(bible_df['chapter'] == chapter) & (bible_df['verse'] == verse)]
                passage_details = "{} Chapter : {}, Verse : {}".format(book_name, chapter, verse)
                st.info(passage_details)
                passage = "{}".format(selected_passage['text'].values[0])
                st.write(passage)
            except:
                st.warning("Book out ot Range")
        
        with c2:
            chapter_list = range(20)
            verse_list = range(20)
            ch_choice = random.choice(chapter_list)
            vs_choice = random.choice(verse_list)
            random_book_name = random.choice(book_list)

            rand_bible_df = df[df["book"] == random_book_name]

            try:
                randomly_selected_passage = rand_bible_df[(rand_bible_df['chapter'] == ch_choice) & (rand_bible_df['verse'] == vs_choice)]
                mytext = randomly_selected_passage["text"].values[0]
            except:
                mytext = rand_bible_df[(rand_bible_df['chapter'] == 1) & (rand_bible_df['verse'] == 1)]["text"].values[0]
            
            stc.html(HTML_RANDOM_TEMPLATE.format(mytext), height=300)
        
        search_term = st.text_input("Term/Topic")
        with st.expander("View Results"):
            retrieved_df = df[df['text'].str.contains(search_term)]
            st.dataframe(retrieved_df[["book", "chapter", "verse", "text"]])


    elif choice == "MultiVerse":
        st.subheader("Multi Verse Analysis")
        book_list = df['book'].unique().tolist()
        book_name = st.sidebar.selectbox("Book", book_list)
        chapter = st.sidebar.number_input("Chapter", 1)
        bible_df = df[df['book'] == book_name]
        all_verse = bible_df['verse'].unique().tolist()
        verse = st.sidebar.multiselect("Verse", all_verse, default=1)
        selected_pssage = bible_df.iloc[verse]
        passage_details = "{} Chapter : {} Verse : {}".format(book_name, chapter, verse)
        st.info(passage_details)

        col1, col2 = st.columns(2)
        docx = " ".join(selected_pssage['text'].tolist())

        with col1:
            st.info("Details")
            for i, row in selected_pssage.iterrows():
                st.write(row['text'])
        with col2:
            st.success("Study Mode")
            with st.expander("Visualize Entities"):
                render_entities(docx)

    else:
        st.subheader("About Bible App")


if __name__ == '__main__':
    main()