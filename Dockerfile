FROM python:3.7.4-slim-stretch
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python3 -m pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chown -R www-data:www-data /usr/src/app
USER www-data
EXPOSE 8080
CMD ["gunicorn", "-c", "gunicorn_config.py", "wsgi"]
