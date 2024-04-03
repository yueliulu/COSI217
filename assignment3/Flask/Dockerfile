FROM python:3.11-slim
WORKDIR /app_flask
COPY . /app_flask
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
EXPOSE 5000
ENV NAME COSI217
CMD ["python", "app_flask.py"]