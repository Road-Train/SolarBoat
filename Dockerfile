# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Check the OS type and adjust configurations accordingly
# ARG OS_TYPE
# RUN if [ "$OS_TYPE" = "linux" ]; then \
#         # Linux-specific configurations \
#     else \
#         # Windows-specific configurations \
#     fi

# Run the script when the container launches
CMD ["python", "./ReadControllerInputs.py"]
