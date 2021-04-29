FROM python:3.8

COPY requirements.txt /webapp/requirements.txt

WORKDIR /webapp

RUN apt get update

RUN pip install -r requirements.txt

COPY webapp/* webapp/

ENTRYPOINT ["python"]

CMD ["app.py"]
