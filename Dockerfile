# Use an official Python runtime based on Alpine 3.10 as a parent image
FROM python:3.9-bullseye

# The environment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# Declare build arguments for our secrets
ARG ENVIRONMENT
ARG PINECONE_KEY
ARG OPENAI_KEY
ARG AUTH0_CLIENT_ID
ARG AUTH0_CLIENT_SECRET
ARG AWS_DEFAULT_REGION
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG REDIS_USERNAME
ARG REDIS_HOST
ARG REDIS_PASSWORD

# Set the environment variables in the container
ENV ENVIRONMENT=$ENVIRONMENT
ENV PINECONE_KEY=$PINECONE_KEY
ENV OPENAI_KEY=$OPENAI_KEY
ENV AUTH0_CLIENT_ID=$AUTH0_CLIENT_ID
ENV AUTH0_CLIENT_SECRET=$AUTH0_CLIENT_SECRET
ENV AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV REDIS_USERNAME=$REDIS_USERNAME
ENV REDIS_HOST=$REDIS_HOST
ENV REDIS_PASSWORD=$REDIS_PASSWORD


# Install the requirements
COPY /requirements.txt /src/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set the working directory in the container
WORKDIR /src

# Copy the current directory contents into the container at /app
COPY . /src/

# Expose the port the app runs in
EXPOSE 80

# Serve the app with Uvicorn for production
CMD ["uvicorn", "src.server.app:app", "--host", "0.0.0.0", "--port", "80"]
