FROM python:3

WORKDIR /usr/src/app

COPY cron-job/* ./

CMD [ "python", "cron.py" ]
