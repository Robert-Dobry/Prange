FROM python:latest

WORKDIR /app

COPY src/ /app/

RUN pip install flask && pip install numpy

CMD [ "python3 src/server.py" ]