FROM python:alpine3.7
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["app.py"]