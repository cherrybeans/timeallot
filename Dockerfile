# Start with a Python image.
FROM python:3.6

# Some stuff that everyone has been copy-pasting
# since the dawn of time.
ENV PYTHONUNBUFFERED 1

# Install some necessary things.
RUN apt-get update
RUN apt-get install -y swig libssl-dev dpkg-dev netcat

# Copy all our files into the image.
RUN mkdir /timeallot
WORKDIR /timeallot
COPY . /timeallot/

# Install our requirements.
RUN pip install -U pip
RUN pip install -Ur requirements/production.txt

CMD gunicorn timeallot.wsgi:application -b 0.0.0.0:8000 --access-logfile -


