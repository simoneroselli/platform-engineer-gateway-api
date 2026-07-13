# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install the necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your operator code into the container
COPY operator.py .

# Set the command to run the Kopf operator
# This will start the reconciliation loop
CMD ["kopf", "run", "operator.py", "--verbose"]