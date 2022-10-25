import streamlit as st
import pandas as pd
import os
import io
from io import BytesIO
from gtts import gTTS


st.set_page_config(
    page_title="easy edit app", page_icon="📖", layout="centered"
)
st.image("icon.png", width=300)
st.subheader("Hey there 🙋🏾‍♀️")
st.subheader("This is an app to make editing easier by listening to chapters")
st.write("connect with me on [Linkedin](https://www.linkedin.com/in/ifeoma-igwe-69b84b16b/)")

voices = ["Default accent","Nigerian accent"]
voice = st.sidebar.selectbox("Select Voice", voices)

if voice == "Default accent":
    language = 'en'
    tld_lang = 'com'
elif voice == "Nigerian accent":
    language = 'en'
    tld_lang = 'com.ng'

#uploaded_file used to be f
uploaded_file = st.file_uploader("", type=[".txt"])
st.info(f"""upload your chapters in .txt files""")


if uploaded_file is not None:
    fileName = st.text_input("Enter the name of the output file and click enter", "Type here")

    raw_text = str(uploaded_file.read(),"utf-8")
    #The code below will write out text file
    #st.write(raw_text)

    output = gTTS(text = raw_text, lang = language, tld=tld_lang, slow = False)
    output.save(fileName)

    audio_file = open(fileName, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/wav',start_time=0)
    
    st.write(
        "Download file by clicking on ⋮ "
    )

