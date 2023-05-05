# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the application will run on
EXPOSE 8000

# Start the application with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
