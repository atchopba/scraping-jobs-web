# The docker image we base our one from
FROM python:3.10.1

# Information of the maintainer of this file
MAINTAINER "Who I am <atchopba@gmail.com>"

ADD . /

RUN python -m pip install --upgrade pip 

RUN pip install -r requirements.txt

WORKDIR .

EXPOSE 5000

CMD ["python", "wsgi.py"]
