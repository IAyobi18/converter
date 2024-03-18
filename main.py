import streamlit as st

st. title("Currency Converter")
st.text_input("Enter amount:")
st.radio("Select currency:", ["GBP to USD", "GBP to JPY", "GBP to EUR"])

col1, col2 = st.columns([1,1])

with col1:
    st.text("Converted amount:")
with col2:
    st.text("900")


