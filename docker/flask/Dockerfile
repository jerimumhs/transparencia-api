FROM python:3.7
ENV PYTHONUNBUFFERED 1

ENV FLASK_APP transparencia_api
ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE 5000

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

WORKDIR /app

CMD ["flask", "run"]
