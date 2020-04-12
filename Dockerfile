# The docker image we base our one from
FROM python:3.7.7

# Information of the maintainer of this file
MAINTAINER "Who I am <atchopba@gmail.com>"

RUN mkdir /app

WORKDIR /app

ADD . /app/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]