import streamlit as st
from groq import Groq

st.set_page_config(page_title="Soumya - Vicky ki AI", page_icon="🤖")
st.title("🤖 Soumya - Vicky ki AI")
st.write("Namaste Vicky bhai! Bolo kya karu?")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

user_input = st.text_input("Bolo mujhse:", placeholder="Jaise: YouTube kholo")

user_lower = user_input.lower() if user_input else ""

if "youtube" in user_lower:
    st.link_button("▶️ YouTube Khol", "https://youtube.com")
elif "insta" in user_lower:
    st.link_button("📸 Instagram Khol", "https://instagram.com")
elif "free fire" in user_lower or "ff" in user_lower:
    st.link_button("🔥 Free Fire Khol", "https://play.google.com/store/apps/details?id=com.dts.freefireth")
elif user_input:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": user_input}]
    )
    st.write("**Soumya:** " + response.choices[0].message.content)

st.caption("Sirf Vicky bhai ke liye ❤️")
