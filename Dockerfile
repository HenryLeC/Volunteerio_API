# Use the Python3.9.0b5 image
FROM python:3.8.5-buster

# Add requirement.txt
ADD requirements.txt /app/

# Set the working directory to /app
WORKDIR /app

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app 
ADD . /app

# run the command to start uWSGI
CMD ["uwsgi", "app.ini", "--wsgi-disable-file-wrapper"]