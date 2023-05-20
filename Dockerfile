FROM python:3.11-slim

ENV user="Hello" \ 
    number=12345

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080

CMD ["flask","run","--host=0.0.0.0", "--port=8080" ]