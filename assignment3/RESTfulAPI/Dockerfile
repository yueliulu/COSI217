FROM python:3.11-slim
WORKDIR /app_fastapi
COPY . /app_fastapi
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
EXPOSE 8000
ENV NAME COSI217
CMD ["uvicorn", "app_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]