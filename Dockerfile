FROM 
tiangolo/uvicorn-gunicorn:python3.8-slim

ENV PYTHONUNBUFFERED True

COPY ../

ENV PORT 8081

RUN pip install --no-cache-dir -r 
requirements.txt

CMD exec gunicorn --bind :$PORT --workers 
1 --worker-class 
uvicorn.workers.UvicornWorker --threads 8 
main_1:app
