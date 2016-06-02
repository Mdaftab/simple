FROM ubuntu

MAINTAINER church@docker.com

EXPOSE 5001

RUN sudo apt-get update && apt-get -y install \
	python-pip

RUN sudo pip install flask

COPY / /backend/

WORKDIR /backend

RUN chmod a+x /backend/run.py

RUN ls -la

CMD ["python", "/backend/run.py"]



