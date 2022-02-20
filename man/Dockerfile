# pull official base image
FROM python:3.7

# accept arguments
ARG PIP_REQUIREMENTS=production.txt

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip setuptools

# create user for the Django project
RUN useradd -ms /bin/bash myproject

# set current user
USER myproject

# set work directory
WORKDIR /home/myproject

# create and activate virtual environment
RUN python3 -m venv env

# copy and install pip requirements
COPY --chown=myproject ./src/django-myproject/requirements /home/django-myproject/requirements/
RUN ./env/bin/pip install -r /home/django-myproject/requirements/${PIP_REQUIREMENTS}

# copy Django project files
COPY --chown=myproject ./src/django-myproject /home/django-myproject/
