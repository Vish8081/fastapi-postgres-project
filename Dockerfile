FROM python:3.9

WORKDIR /app

# Install dependencies first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Environment variables
ENV PYTHONPATH=/app
ENV SQLALCHEMY_DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]