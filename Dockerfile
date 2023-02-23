FROM python:3.9-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /server
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . . 
CMD python manage.py runserver 0.0.0.0:80

