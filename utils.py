import streamlit as st 
import streamlit.components.v1 as stc 

import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')


HTML_RANDOM_TEMPLATE = """
<div style='padding:10px;background-color:#E1E2E1;
			border-radius: 8px 34px 9px 26px;
-moz-border-radius: 8px 34px 9px 26px;
-webkit-border-radius: 8px 34px 9px 26px;
border: 2px ridge #000000;'>
<h5>Verse of the Day</h5>
<p>{}</p></div>
"""


HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">StreamBible App </h1>
    </div>
    """

def render_entities(raw_text):
	docx = nlp(raw_text)
	html = displacy.render(docx,style='ent')
	html = html.replace("\n\n","\n")
	result = HTML_WRAPPER.format(html)
	stc.html(result,height=1000)