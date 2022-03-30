FROM python:3.9-alpine

WORKDIR /permissions

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "migrate"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]