FROM python:3

WORKDIR /opt/gm

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["tail", "-f", "docker/requirements.txt"]
