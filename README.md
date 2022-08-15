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

Use the `py39-student-acceptance-project` kernel


## Running it locally

Train a model:

```bash
pipenv run python train.py 
```

Run streamlit:

```bash
pipenv run streamlit run front.py
```

## Docker

Building it with docker:

```bash
docker build -t student-acceptance-project:v01 .
```

Running it:

```bash
docker run -it --rm \
    -p 8501:8501 \
    student-acceptance-project:v01
```

## Cloud

This application is deployed to streamlit cloud:

https://alexeygrigorev-student-acceptance-project-front-bv02me.streamlitapp.com/