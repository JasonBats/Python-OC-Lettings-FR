FROM python:3.10-slim
WORKDIR /app
ARG SECRET_KEY
ENV SECRET_KEY=${SECRET_KEY}
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]