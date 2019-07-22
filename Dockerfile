FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /SakaBackend
WORKDIR /SakaBackend
COPY . /SakaBackend/
RUN pip install -r requirements.txt
