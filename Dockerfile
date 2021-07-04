# pull python 3 image from docker hub or from local fs
FROM python:3.8

LABEL name="Pragyanshu Rai" \
email="pragyanshur@gmail.com"

# -----------------------------------------------------------------------------------------

# All the two variables defined below are for twilio account
# My account sid
ENV TWILIO_ACC_SID="ACa7eba6c51aa678dbaaad00212c381c9d"

# My Auth-token
ENV TWILIO_AUTH_TOKEN="18481ad5aaf322dcd4607e52abe00f70"

# Twillio phone number
ENV TWILIO_NUMBER="+18505839086"

# -----------------------------------------------------------------------------------------

# This is my regular phone number
ENV MY_PHONE_NUMBER="+917893153980"

# -----------------------------------------------------------------------------------------

# All the the variables defined are for aws S3 account
# Access Key Id
ENV AWS_ACCESS_KEY_ID="AKIA2VJYNI6SKU64NLXX"

# Access Key
ENV AWS_SECRET_ACCESS_KEY="ivWpoF/xJafu3ULx1rLILTOi2LOhuh/1ehFMQGxS"

# S3 Storage name
ENV AWS_STORAGE_BUCKET_NAME="pragyanshu-cms"

# -----------------------------------------------------------------------------------------

# All the the variables defined are for the system mail account
# System Email
ENV SYSTEM_EMAIL="noreply.services.2001@gmail.com"

# Email Passkey
ENV SYSTEM_EMAIL_PASSKEY="cxzifunjhbptvsml"

# Email Host
ENV SYSTEM_EMAIL_HOST="smtp.gmail.com"

# Email Port
ENV SYSTEM_EMAIL_PORT=587

ENV PYTHONBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 
ENV DJ_PORT=8000
ENV MY_PHONE_NUMBER="+917893153980"

# create a directory 'apps'
RUN mkdir /apps

# add all the files in the apps directory
ADD . /apps/ 

# make /apps the pwd
WORKDIR /apps

# run a pip command to install everything listed in the requirements.txt file
# install environment dependencies
# Install project dependencies
RUN pip install -r requirements.txt; \
pip3 install --upgrade pip; \
apt-get autoremove; 

# expose container port number
EXPOSE 8000

CMD gunicorn CMS.wsgi:application --bind 0.0.0.0:$DJ_PORT
# CMD [ "pip", "freeze" ]