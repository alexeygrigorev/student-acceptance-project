import streamlit as st

st.set_page_config(
    page_title="Student college acceptance",
    page_icon="🎓"
)

st.write("""
## Student College Acceptance prediction

In this project we predict if a student will be accepted to
college or not.
""")

type_school = st.selectbox(
    'School type',
    ('Academic', 'Vocational')
)

school_accreditation = st.selectbox(
    'School accreditation',
    ('A', 'B')
)

gender = st.selectbox(
    'Gender',
    ('Male', 'Female')
)

interest = st.selectbox(
    'Student interest',
    ('Very Interested', 'Quiet Interested', 'Uncertain', 'Less Interested', 'Not Interested')
)

parent_age = st.slider(
    'Age of the parent',
    min_value=40,
    max_value=65,
    value=50
)

parent_salary = st.slider(
    'The salary of the parent',
    min_value=1000000,
    max_value=10000000,
    value=4600000,
    step=100000
)

house_area = st.slider(
    'The areas of the house',
    min_value=20,
    max_value=120,
    value=60
)

average_grades = st.slider(
    'Average grade',
    min_value=75,
    max_value=100,
    value=85
)

residence = st.selectbox(
    'Residence',
    ('Urban', 'Rural')
)

parent_was_in_college = st.selectbox(
    'Was the parents in college?',
    ('Yes', 'No')
)

student = {
    'type_school': type_school.value(),
    'school_accreditation': 'A',
    'gender': 'Male',
    'interest': 'Uncertain',
    'residence': 'Rural',
    'parent_age': 48,
    'parent_salary': 7160000,
    'house_area': 71.0,
    'average_grades': 88.46,
    'parent_was_in_college': True,
}


st.write("""
This project was done as a part of [the project-of-the-week 
initiative at DataTalks.Club](https://github.com/DataTalksClub/project-of-the-week/blob/main/2022-08-14-frontend.md).
""")