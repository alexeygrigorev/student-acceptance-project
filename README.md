## Student Acceptance Prediction

In this project, we develop a model for predicting if a student will be admitted to college or not

This project is done as a part of [Project of the Week at DataTalks.Club](https://github.com/DataTalksClub/project-of-the-week/blob/main/2022-08-14-frontend.md)

Dataset: https://www.kaggle.com/datasets/mahwiz/school-data


## Setup

Install dependencies

```bash
pipenv install --dev
```

Add Jupyter kernel:

```bash
pipenv run python -m ipykernel install --user --name="py39-student-acceptance-project"
```

Run jupyter:

```bash
jupyter notebook
```

Use the `student-acceptance-project` kernel


## Running it locally

Train a model:

```bash
pipenv run python train.py 
```

Serve it:

```bash
pipenv run python serve.py
```

Send a request:

```bash
REQUEST='{
    "type_school": "Academic",
    "school_accreditation": "A",
    "gender": "Male",
    "interest": "Uncertain",
    "residence": "Rural",
    "parent_age": 48,
    "parent_salary": 7160000,
    "house_area": 71.0,
    "average_grades": 88.46,
    "parent_was_in_college": true
}'

URL="http://localhost:9696/predict"

curl -X POST \
    -d "${REQUEST}" \
    -H "Content-Type: application/json" \
    ${URL}
```