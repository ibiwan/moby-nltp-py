FROM python:3
WORKDIR /usr/src/app
RUN pip install nltk 
RUN pip install matplotlib
RUN python -m nltk.downloader popular
