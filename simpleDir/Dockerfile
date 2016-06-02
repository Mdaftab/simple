FROM ubuntu

RUN sudo apt-get update && apt-get -y install python-pip

RUN sudo pip install flask

COPY / /simpleDir

WORKDIR /simpleDir

RUN chmod a+x /simpleDir/run.py

CMD ["python", "/simpleDir/run.py"]



