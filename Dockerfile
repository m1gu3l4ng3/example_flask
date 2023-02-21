FROM python:3.10

WORKDIR /opt

COPY ./requirements.txt /opt/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /opt/requirements.txt

COPY ./app /opt/app

WORKDIR /opt/app

CMD gunicorn app:app -w 2 --threads 2 -b 0.0.0.0:8000 --access-logfile -
