 as st
from groq imimportport Groq
from PIL import Image

st.set_page_config(page_title="Soumya - Vicky ki AI", page_icon="🤖")

st.title("🤖 Soumya - Vicky ki AI")
st.write("Namaste! Mujhe Vivek Vishwakarma aka Vicky ne banaya hai")

import streamlit as st
from groq import Groq
from PIL import Image

st.set_page_config(page_title="Soumya - Vicky ki AI", page_icon="🤖")

st.title("🤖 Soumya - Vicky ki AI")
st.write("Namaste! Mujhe Vivek Vishwakarma aka Vicky ne banaya hai")

# Line 10-13 hata di, ab seedha secrets se key legi
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

tab1, tab2 = st.tabs(["💬 Baat Karo", "📸 Photo Bhejo"])

with tab1:
    user_input = st.text_input("Kuch bhi bolo mujhse:")
    if user_input:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": user_input}],
            model="llama-3.1-8b-instant"
        )
        st.write(response.choices[0].message.content)

with tab2:
    uploaded_file = st.file_uploader("Photo bhejo yaha:", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Teri photo", use_column_width=True)
        st.write("Photo mil gayi  bhai!")

if api_key:
    client = Groq(api_key=api_key)
    
    tab1, tab2 = st.tabs(["💬 Baat Karo", "📸 Photo Bhejo"])
    
    with tab1:
        user_input = st.text_input("Kuch bhi bolo mujhse:")
        if user_input:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": user_input}],
                model="llama-3.1-8b-instant"
            )
            st.write(response.choices[0].message.content)
    
    with tab2:
        uploaded_file = st.file_uploader("Photo bhejo yaha:", type=["jpg", "png", "jpeg"])
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Teri photo", use_column_width=True)
            st.write("Photo mil gayi Vicky bhai! Ab iske baare me pucho mujhse")
            
            question = st.text_input("Photo ke baare me kya puchna hai?")
            if question:
                st.write("Abhi photo samajhne wali AI jodni baaki hai. Par tu puch, main try karungi 😄")
