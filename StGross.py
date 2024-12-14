import streamlit as st
st.title("Gross Salary Calculator")
basic_salary=st.number_input("Enter your Basic salary:",min_value=0,step=1)
if st.button("calculate Gross Salary"):
    hra=0
    da=0
    if basic_salary<10000:
        hra = (67 * basic_salary) / 100
        da = (73 * basic_salary) / 100
    elif basic_salary < 20000:
        hra = (69 * basic_salary) / 100
        da = (76 * basic_salary) / 100
    else:
        hra = (73 * basic_salary) / 100
        da = (89 * basic_salary) / 100
    gs = hra + da + basic_salary
    st.success(f"The Gross Salary is {gs}")