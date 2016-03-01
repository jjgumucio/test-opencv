#!/bin/bash

# Create directory structure
mkdir opencv-worker && cd opencv-worker
mkdir libs

# Get API client libs and image processing script
gsutil cp gs://opencv-worker/libs/*.py ./libs
gsutil cp gs://opencv-worker/task_getter.py .
gsutil cp gs://opencv-worker/file_reference_proof.py .
touch libs/__init__.py

easy_install --upgrade google-api-python-client

# Run image processing script
python file_reference_proof.py


