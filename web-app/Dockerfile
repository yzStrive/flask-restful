FROM python:3
#auto create folder
WORKDIR /home/www/app
COPY ./requirements.txt /home/www/app
#google翻译接口需要在python中用到js，需要有V8的环境
RUN apt-get update && apt-get install -y nodejs npm
RUN pip install -r /home/www/app/requirements.txt
