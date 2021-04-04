FROM python:3.9
WORKDIR /flask-app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    make \
    gcc
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt
COPY . .
RUN python3 driver.py
CMD ["python3", "-m", "flask", "run"]