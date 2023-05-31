FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /api
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
# ENTRYPOINT ["python", "manage.py"]
# CMD ["runserver"]
EXPOSE 8000
RUN ["chmod", "+x", "docker-entrypoint.sh"]
ENTRYPOINT [ "./docker-entrypoint.sh" ]