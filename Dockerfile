FROM python:3.11-slim

WORKDIR /app

# Copy only app (not test runner)
COPY exercise_2/ ./exercise_2/

# Install as editable package (optional)
RUN pip install --upgrade pip

# Entrypoint to run calculator
ENTRYPOINT ["python", "-m", "exercise_2"]
