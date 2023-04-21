FROM python:3.11.2-alpine

WORKDIR /app

COPY . /app

ENV PORT=8000

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

COPY app.py .

CMD ["python", "/app/app.py"]