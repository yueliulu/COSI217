# Assignment 3 - Docker Containers

In this assignment, I created a new code base which includes the RESTfulAPI, Flask, and Streamlit in previous assignments, and created Docker images for them. This includes a Dockerfile for each of three elements, and a docker-compose.yml so all functionality can be accessed simultaneously from the host.

A. Run Separately

To run one webserver individually, direct to the corresponding folder and build the Docker image then run it.
- RESTfulAPI
```
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app
```
- Flask
```
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```
- Streamlit
```
docker build -t streamlit-app .
docker run -p 8501:8501 streamlit-app
```

B. Run All

To run all three, direct to assignment3 folder and run the below command in terminal
```
docker-compose up
```

C. Use Server
After start the server, you can use each server by following the corresponding links:
- RESTfulAPI
```
http://localhost:8000
```
- Flask
```
http://localhost:5000
```
- Streamlit
```
http://localhost:8501
```