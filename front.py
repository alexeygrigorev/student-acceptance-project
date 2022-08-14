import json
import pickle

import streamlit as st


st.set_page_config(
    page_title="Student college acceptance",
    page_icon="🎓"
)

st.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache
def load_model():
    print('loading the model...')

    model_file = 'artifacts/pipeline.bin'

    print('loading the model...')
    with open(model_file, 'rb') as f_in:
        pipeline = pickle.load(f_in)

    return pipeline


pipeline = load_model()


st.write("""
## Student College Acceptance prediction

In this project we predict if a student will be accepted to
college or not.
""")


col11, col12, col13 = st.columns(3)

type_school = col11.selectbox(
    'School type',
    ('Academic', 'Vocational')
)

school_accreditation = col12.selectbox(
    'School accreditation',
    ('A', 'B')
)

gender = col13.selectbox(
    'Gender',
    ('Male', 'Female')
)


col41, col42, col43 = st.columns(3)

interest = col41.selectbox(
    'Student interest',
    ('Very Interested', 'Quite Interested',
     'Uncertain', 'Less Interested', 'Not Interested')
)

residence = col42.selectbox(
    'Residence',
    ('Urban', 'Rural')
)

parent_was_in_college = col43.selectbox(
    'Was the parents in college?',
    ('Yes', 'No')
)


col21, col22 = st.columns(2)

parent_age = col21.slider(
    'Age of the parent',
    min_value=40,
    max_value=65,
    value=50
)

average_grades = col22.slider(
    'Average grade',
    min_value=75,
    max_value=100,
    value=85
)


col31, col32 = st.columns(2)

parent_salary = col31.slider(
    'Parent salary:',
    min_value=1000000,
    max_value=10000000,
    value=4600000,
    step=100000
)

house_area = col32.slider(
    'House area',
    min_value=20,
    max_value=120,
    value=60
)


student = {
    'type_school': str(type_school),
    'school_accreditation': str(school_accreditation),
    'gender': str(gender),
    'interest': str(interest),
    'residence': str(residence),
    'parent_age': int(parent_age),
    'parent_salary': int(parent_salary),
    'house_area': int(house_area),
    'average_grades': int(average_grades),
    'parent_was_in_college': str(parent_was_in_college) == 'Yes',
}

pred = pipeline.predict_proba(student)[0, 1]
pred = float(pred)

col1_pred, col2_pred = st.columns(2)

col1_pred.write("Probability of acceptance:")

col2_pred.write(f"""
<p class="big-font">
{pred:0.2f}
</p>
""", unsafe_allow_html=True)

st.write(f"""
```
REQUEST='{json.dumps(student, indent=4)}'

URL="http://localhost:9696/predict"

curl -X POST \\
    -d "${{REQUEST}}" \\
    -H "Content-Type: application/json" \\
    ${{URL}}
```
""")

st.write("""
This project was done as a part of [the project-of-the-week 
initiative at DataTalks.Club](https://github.com/DataTalksClub/project-of-the-week/blob/main/2022-08-14-frontend.md).
""")