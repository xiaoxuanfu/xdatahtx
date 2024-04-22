# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy only the dependencies installation files
COPY pyproject.toml poetry.lock* /app/

# Install dependencies using poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy the local code to the container's workspace
ADD . /app

# Expose the port the app runs on
EXPOSE 8001

# Run the application
CMD ["uvicorn", "asr_api:app", "--host", "0.0.0.0", "--port", "8001"]
