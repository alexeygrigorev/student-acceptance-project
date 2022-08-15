FROM python:3.9-slim

RUN pip install pipenv 

WORKDIR /app

COPY [ "Pipfile", "Pipfile.lock", "./" ]

RUN pipenv install --system --deploy

COPY "front.py" "front.py"
COPY "artifacts/pipeline.bin" "artifacts/pipeline.bin"

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run", "front.py" ]