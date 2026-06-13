FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install yamllint

RUN apt-get update && \
    apt-get install -y curl

RUN curl -LO "https://dl.k8s.io/release/v1.33.1/bin/linux/amd64/kubectl" && \
    chmod +x kubectl && \
    mv kubectl /usr/local/bin/kubectl

COPY . .

CMD ["python", "app/main.py"]