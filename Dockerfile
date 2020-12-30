FROM ubuntu:latest
RUN apt update -y
RUN apt install -y python3-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ['python']
CMD ['entry.py']