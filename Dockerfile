FROM python:3.7
ENV PYTHONUNBUFFERED 1

EXPOSE 5000

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

WORKDIR /app

CMD ["flask", "run"]
