import streamlit as st
st.title("Grade Calculator")
project=st.number_input('Enter the project score:',min_value=1,step=1)
external=st.number_input('Enter external score:',min_value=1,step=1)
internal=st.number_input('Enter internal score:',min_value=1,step=1)
if st.button("grade"):
    if project >=50 and internal >=50 and external>=50:
        total=((70*project)+(10*internal)+(20*external))/100
        st.write(f'total score is : {total}')
        if total >=90:
            st.success('A grade')
        elif total >80:
            st.success('B grade')
        else:
            st.success('C grade')
    else:
        if project < 50:
            st.error(f'Failed in project and score is : {project}')
        if external < 50:
            st.error(f'Failed in external and score is : {external}')
        if internal < 50:
            st.error(f'Failed in internal and score is : {internal}')