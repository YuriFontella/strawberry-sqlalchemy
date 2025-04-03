FROM python:3.13.1

WORKDIR /var/www

RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENV PYTHON_ENV="production"

CMD ["uvicorn", "--log-level", "error", "--host", "0.0.0.0", "--port", "6003", "app:app"]