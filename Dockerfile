FROM pamtrak06/ubuntu14.04-grib
RUN apt-get install -y python python-grib
ADD  . /code
WORKDIR /code
CMD python main.py