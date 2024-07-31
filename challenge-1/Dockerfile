FROM alpine:3.20

# Install Python 3.8
RUN apk add --no-cache python3

WORKDIR /app

COPY . /app

# Upgrade pip and install dependencies
RUN pip3 install -U pip && pip3 install -r requirements.txt || echo "Failed to install dependencies"

WORKDIR /app

EXPOSE 8000

CMD ["python3", "challenge-1.py"]