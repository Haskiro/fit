FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /api
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT [ "sh", "entrypoint.sh" ]
EXPOSE 8000