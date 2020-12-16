FROM neo4j

RUN apt update -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install pandas
RUN pip3 install sklearn
RUN pip3 install py2neo
RUN pip3 install --upgrade py2neo
RUN mkdir -p /usr/src/app
COPY . /usr/src/app