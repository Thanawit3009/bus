FROM python:3.11

WORKDIR /lab

COPY . .

RUN pip install django

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000

# รัน Django server บน 0.0.0.0:8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
