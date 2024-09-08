# Dockerfile

# Use the official Python image from the Docker Hub
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the Django application code into the container
COPY . /app/

# Run Django migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Expose port 8000 for Django
EXPOSE 8000

# Run the Django development server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog.wsgi:application"]
