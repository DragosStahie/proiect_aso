FROM python:3.10

ENV DockerHOME=/home/aso/chatapp

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . $DockerHOME

RUN pip install -r requirements.txt

EXPOSE 8000