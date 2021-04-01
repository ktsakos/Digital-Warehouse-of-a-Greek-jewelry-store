FROM ubuntu
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y update
RUN apt-get install -y python3
RUN apt-get -y update
RUN apt-get install -y python3-pip
ENV DEBIAN_FRONTEND noninteractive #a command to have zero interaction while installing or upgrading a system - all answers take their default values
RUN apt-get install python3-tk -y
RUN pip3 install  psycopg2-binary
WORKDIR /code
COPY ./code /code
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3","jewelery_gui2.0.py"]