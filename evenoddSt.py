import streamlit as st
st.title("Even/Odd")
num1=st.number_input("Enter number",min_value=1,step=1)
if st.button("Even/odd"):
    if num1%2==0:
        st.success("even")
    else:
        st.error("Odd")