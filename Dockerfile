#FROM python:2.7.15

FROM alpine:3.1

#RUN apt update \
#&& apt upgrade -y \
#    && apt install --no-install-recommends --no-install-suggests -y python python-pip 
#    && pip install flask

RUN apk add --update python py-pip

COPY ./app /app

WORKDIR /app

EXPOSE 80

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["main.py"]

ADD VERSION .
