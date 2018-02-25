FROM python:3

WORKDIR .

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p uploads

COPY . .

EXPOSE 5000

CMD [ "python", "./server.py" ]
