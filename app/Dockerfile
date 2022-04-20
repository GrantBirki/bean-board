FROM python:3.9.6-alpine3.14

# permissions and nonroot user for tightened security
RUN adduser -D nonroot

# install curl
RUN apk add curl

# create file strcuture
RUN mkdir /home/app/ && chown -R nonroot:nonroot /home/app
RUN mkdir -p /var/log/flask-app && touch /var/log/flask-app/flask-app.err.log && touch /var/log/flask-app/flask-app.out.log

# assign permissions to flask-app
RUN chown -R nonroot:nonroot /var/log/flask-app
WORKDIR /home/app
USER nonroot

# venv
ENV VIRTUAL_ENV=/home/app/venv

# python setup
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN export FLASK_APP=app.py
COPY --chown=nonroot:nonroot requirements.txt .
RUN pip install -r requirements.txt

# copy all the files to the container
COPY --chown=nonroot:nonroot . .

# define the port number the container should expose
EXPOSE 5000

ENTRYPOINT ["python3"] 
CMD ["app.py"]
