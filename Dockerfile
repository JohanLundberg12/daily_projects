# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Copy the local files to the container
COPY . /app

# Set the working directory in the container
WORKDIR /app

# Install project-level dependencies
RUN apt-get update \
    && apt-get install -y git \
    && pip install -r requirements.txt



# Clone the repository and install dependencies
RUN git clone https://github.com/Lightning-AI/lit-gpt /app/lit-gpt
WORKDIR /app/lit-gpt
RUN pip install -r requirements.txt
RUN pip install -r requirements-all.txt
RUN pip install huggingface_hub
RUN pip install tokenizers 

# Download the model checkpoint and convert it
RUN python scripts/download.py --repo_id microsoft/phi-1_5 && \
    python scripts/convert_hf_checkpoint.py --checkpoint_dir checkpoints/microsoft/phi-1_5

WORKDIR /app

# Expose the required port for the Flask app
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]