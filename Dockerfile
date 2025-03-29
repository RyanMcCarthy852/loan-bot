# Use the official Python 3.12 image from the Docker Hub
FROM python:3.12

WORKDIR /app
COPY . /app

RUN pip install .

EXPOSE 80

ENTRYPOINT ["python", "main.py"]