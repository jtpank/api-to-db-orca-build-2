FROM python:3.7-alpine
RUN pip install --upgrade pip
RUN apk add --no-cache build-base
RUN apk add --no-cache mariadb-dev

RUN adduser -D myuser
USER myuser
WORKDIR /home/myuser

COPY --chown=myuser:myuser requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

ENV PATH="/home/myuser/.local/bin:${PATH}"

COPY --chown=myuser:myuser . .
EXPOSE 5000
CMD ["python", "app.py"]
