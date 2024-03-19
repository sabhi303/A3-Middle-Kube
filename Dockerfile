FROM python:3.9

WORKDIR /app

COPY a3.py .

CMD ["python", "a3.py"]
   