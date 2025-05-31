FROM python:3.11-slim

WORKDIR /app
COPY hello.py .
COPY requirements.txt .

RUN python -r install requirements.txt
RUN apt-get update && apt-get install -y git && git clon

CMD ["python", "hello.py"]



