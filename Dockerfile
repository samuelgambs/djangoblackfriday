FROM python:3.6

COPY . /srv/maxfriday
WORKDIR /srv/maxfriday

RUN apt-get update && apt-get install python-mysqldb && \
    pip install -r requirements.txt && \
    cp maxmilhas/production_settings_sample.py maxmilhas/production_settings.py

CMD ["python", "manage.py", "runserver", "0.0.0.0:443"]

EXPOSE 443
