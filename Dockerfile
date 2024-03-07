FROM ubuntu
WORKDIR /tokenauth/

RUN apt-get update -y 
RUN apt install nano -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip install Django==4.0
RUN pip install psycopg2-binary
RUN pip install python-barcode
RUN pip install mysql-connector-python
RUN pip install mailjet_rest
RUN pip install tzdata
RUN pip install pytz
COPY . ./
COPY tokenbag/dependencias/models.py /usr/local/lib/python3.10/dist-packages/django/contrib/auth/
COPY tokenbag/dependencias/base.py /usr/local/lib/python3.10/dist-packages/barcode/
COPY templates/technical_404.html /usr/local/lib/python3.10/dist-packages/django/views/templates/
COPY templates/technical_500.html /usr/local/lib/python3.10/dist-packages/django/views/templates/
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8002
CMD python3 manage.py runserver 172.17.0.2:8002
