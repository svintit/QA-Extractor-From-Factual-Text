FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /extractor
WORKDIR /extractor

COPY requirements.txt /extractor/
RUN pip3 install -r requirements.txt

RUN python3 -m spacy download en_core_web_sm

COPY extractor-entrypoint extractor-entrypoint
RUN chmod +x extractor-entrypoint

COPY . /extractor/
