# Use a specific version of Python slim-bullseye for better security
FROM python:3.11.7-slim-bullseye

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=8000 \
    TF_CPP_MIN_LOG_LEVEL=2 \
    PYTHONDONTWRITEBYTECODE=1 \
    # Prevent Python from writing pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    # Prevent Python from buffering stdout and stderr
    PYTHONUNBUFFERED=1

# Create a non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set working directory
WORKDIR /app

# Install system dependencies and clean up in the same layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    # Create necessary directories and set permissions
    && mkdir -p /app/models \
    && chown -R appuser:appuser /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    # Remove pip to reduce attack surface
    pip uninstall -y pip setuptools

# Copy the application code
COPY . .

# Set correct permissions
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose the port the app runs on
EXPOSE $PORT

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:$PORT/docs || exit 1

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]
