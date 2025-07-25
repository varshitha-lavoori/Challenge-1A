# Use an official Python image
FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

COPY extractor.py .

# Install PyMuPDF
RUN pip install pymupdf

ENTRYPOINT ["python", "extractor.py"]
