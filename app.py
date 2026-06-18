import streamlit as st
from groq import Groq

st.set_page_config(page_title="Soumya AI", page_icon="🤖")
st.title("🤖 Soumya - Vicky ki AI")
st.write("Namaste! Mujhe Vicky Vishwakarma ne banaya hai. Batao kya madad karu?")

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=GROQ_API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Soumya se kuch pucho..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        stream = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True
        )
        for chunk in stream:
            full_response += chunk.choices[0].delta.content or ""
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

   
