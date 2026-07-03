# Use a lightweight official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your python script into the container
COPY count_bases.py .

# Run the script when the container starts
CMD ["python", "count_bases.py"]

