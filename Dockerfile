FROM python:3.8-slim

WORKDIR /app
ENV PYTHONPATH="/app"

COPY . /app

RUN apt-get update && apt-get install -y \
    libglib2.0-0 libsm6 libxext6 libxrender-dev libgl1 \
    && pip install --upgrade pip \
    && pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org --break-system-packages -r requirements.txt


CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
