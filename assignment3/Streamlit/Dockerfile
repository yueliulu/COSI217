FROM python:3.11-slim
WORKDIR /app_streamlit
COPY . /app_streamlit
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
EXPOSE 8501
ENV NAME COSI217
CMD ["streamlit", "run", "app_streamlit.py"]