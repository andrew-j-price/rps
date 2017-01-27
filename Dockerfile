FROM alpine:3.4

# Update
RUN apk add --update python py-pip && \
    rm -rf /var/cache/apk/*

# Install app dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Copy app
COPY flask_based /flask/

EXPOSE  5000
CMD ["python", "/flask/app.py"]
