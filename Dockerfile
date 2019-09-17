
# getting python version 3.6 with stretch which brings in ubuntu
FROM python:3.6-stretch

# turtle needs tkinter
RUN sudo apt-get install python3-tk -y

