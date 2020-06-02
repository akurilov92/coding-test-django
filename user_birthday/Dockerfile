FROM python:3
# we want the python output to be sent directly to terminal so that we can see immediately
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt