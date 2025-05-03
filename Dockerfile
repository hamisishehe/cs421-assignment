FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements if available
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port and run Flask app
EXPOSE 5000
CMD ["python", "app.py"]
