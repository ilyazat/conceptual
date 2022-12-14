FROM python:3.10.5-slim-buster

WORKDIR src/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY ./app ./app/

COPY requirements.txt .
RUN pip install --no-cache-dir -r /src/requirements.txt

CMD ["python3" ,"-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
