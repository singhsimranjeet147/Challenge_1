FROM python:3.9-slim

WORKDIR /app


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose port and run the application on port 6001
EXPOSE 6001
CMD ["python", "app.py"]
