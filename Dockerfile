ARG PYTHON_V=3.9.6
ARG CMD_START_FILE=

FROM python:${PYTHON_V}

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

WORKDIR /app

COPY src .

CMD ["python3", "publisher.py"]