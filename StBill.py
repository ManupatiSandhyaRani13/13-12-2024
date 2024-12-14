import streamlit as st
st.title("Shopping Percentage in Salary")
salary=st.number_input('Enter salary:',min_value=1,step=1)
s1=st.number_input('enter shopping 1 amt:',min_value=1,step=1)
s2=st.number_input('enter shopping 2 amt:',min_value=1,step=1)
s3=st.number_input('enter shopping 3 amt:',min_value=1,step=1)
if st.button("Calculate percentage"):
    sum=s1+s2+s3
    per=(sum*100)/salary
    st.success(f'The shopping percentage is {per} %')