FROM python:3.8.4

RUN apt-get update && /usr/local/bin/python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r ./requirements.txt

COPY . .

EXPOSE 8000

ENV UVICORN_HOST=0.0.0.0
ENV UVICORN_PORT=8000
ENV UVICORN_WORKERS=1

CMD "python3" "main.py"
