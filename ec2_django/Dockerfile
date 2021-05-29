FROM python:3.6-alpine

EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev

ADD . /ec2_django

WORKDIR /ec2_django

RUN pip install -r requirements.txt

RUN python django_ec2_project/manage.py makemigrations

RUN python django_ec2_project/manage.py migrate

CMD [ "python", "django_ec2_project/manage.py", "runserver", "0.0.0.0:8000" ]
