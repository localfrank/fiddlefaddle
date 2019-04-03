ARG PYTHON_VERSION

FROM python:$PYTHON_VERSION
LABEL maintainer="Frank WANG <frank.pypy@gmail.com>"

EXPOSE 5000

WORKDIR /app
COPY . /app

RUN python -m pip install -r requirements.txt

CMD ["python", "run.py"]

