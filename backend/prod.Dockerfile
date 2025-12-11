# syntax=docker/dockerfile:1
FROM python:3.11

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1
ARG APP_HOME=/app
# Change working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    unixodbc-dev \
    curl \
    gettext \
    gnupg \
    wget

# Download dependencies as a     separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python3 -m pip install -r requirements.txt


# Create new user and set it's UID to 1000.
ARG UID=1000
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Copy the source code into the container.
COPY . .
# Create static dir and then change user to 'root' to modify static folder's permissions.
USER root
RUN mkdir -p /app/staticfiles
RUN mkdir -p /app/mediafiles
RUN mkdir -p /app/logs
RUN chmod 777 /app/staticfiles
RUN chmod 777 /app/mediafiles
RUN chmod -R 777 /app/logs
RUN chown -R appuser:appuser /app/logs

# Collect static files
#RUN python manage.py collectstatic --noinput --clear

# Run 'compilemessages' cmd to apply translates.
#RUN django-admin compilemessages

# Change user to 'appuser'.
USER appuser

# Run the application.
CMD gunicorn -c gunicorn.conf.py rteknoloji.wsgi:application
#CMD python manage.py runserver 0.0.0.0:8000