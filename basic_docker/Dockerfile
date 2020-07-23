# base image is python3.6 installed debian, can be changed to any other os
FROM python:3.6-stretch

# copying all the files in current path to app folder which can be found in the container also
COPY . /app
# changing dir
WORKDIR /app/

# commands that need to be run in terminal of the image that is being built
RUN apt-get update -y
RUN apt-get install python3-pip python3-dev -y
RUN apt-get install build-essential pkg-config -y

RUN python3 -m pip install requirements.txt

# exposing port so that can be accessed from out side container(from host system) 
EXPOSE 1111
# command 
CMD ["sh","-c","python3 app.py"]
