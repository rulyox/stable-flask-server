FROM python:3

COPY ./app /server
WORKDIR /server

RUN pip3 install -r requirements.txt

CMD ["python", "serve.py"]
