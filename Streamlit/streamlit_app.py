# streamlit_app.py
import streamlit as st

st.title("Hello from Streamlit (PyCharm)")
name = st.text_input("Your name")
if st.button("Greet"):
    st.write(f"Hello, {name} 👋")
