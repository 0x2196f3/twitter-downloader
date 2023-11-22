FROM python:3.10

ADD main.py requirements.txt twitter-media-downloader /app/
RUN pip install -r /app/requirements.txt
CMD ["python3", "/app/main.py"]