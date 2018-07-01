FROM python:3.6.2-jessie

MAINTAINER stainwoortsel <stainwoortsel@gmail.com>

WORKDIR /code

# COPY ./src ./
COPY ./requirements.txt ./
COPY ./imageai-2.0.1-py3-none-any.whl ./
COPY ./resnet50_coco_best_v2.1.0.h5 ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.1/imageai-2.0.1-py3-none-any.whl


RUN cd /code
CMD ["python", "start.py", "console"]