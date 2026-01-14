import streamlit as st

# Profile Name Session
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/connect_brain.png", width=250)

with col2:
    st.title("General Kenobi", anchor=False)
    st.write("Data Analyst Pro")

# Skills Session


