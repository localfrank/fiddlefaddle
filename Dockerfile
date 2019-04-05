ARG PYTHON_VERSION

FROM python:$PYTHON_VERSION
LABEL maintainer="Frank WANG <frank.pypy@gmail.com>"

EXPOSE 5000

WORKDIR /app
COPY . /app

RUN python -m pip install -r requirements.txt
ENV FLASK_APP=run.py

CMD ["flask", "run", "--host=0.0.0.0"]

