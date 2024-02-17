# Assignment 1 - Web Services

In this assignment, I created a RESTful API (fastapi), Flask webserver, and a Streamlit application to access spaCy NER and dependency parsing.  

A. Requirements (Python and modules)

    Python 3.11.7
    spacy 3.7.2
    fastapi 0.109.0
    pydantic 2.5.3
    Flask 2.2.5
    streamlit 1.31.1
    pandas 2.1.4
    altair 5.0.1
    graphviz 0.20.1

B. Run the Code

1. RESTFull API

    Start the RESTFull API by running below command in terminal:

    ```
    uvicorn app_fastapi:app --reload
    ```
    
    Run below commands in terminal to load URLs and see the result

   ```
   # To access index page
   $ curl http://127.0.0.1:8000
   # To access NER
   $ curl http://127.0.0.1:8000/ner -H "Content-Type: application/json" -d@input.txt
   # To access dependencies
   $ curl http://127.0.0.1:8000/dep -H "Content-Type: application/json" -d@input.txt
   ```

   Also accepts a pretty parameter which can reformat the output json

   ```
   $ curl http://127.0.0.1:8000?pretty=true
   $ curl http://127.0.0.1:8000/ner?pretty=true -H "Content-Type: application/json" -d@input.json
   $ curl http://127.0.0.1:8000/dep?pretty=true -H "Content-Type: application/json" -d@input.json
   ```
2. Flask webserver
   
   To start the Flask webserver, run below command in terminal:

   ```
   $ python app_flask.py
   ```
   The webserver is now running on http://127.0.0.1:5000.

   Navigate to this browser, you can input whatever text you want in the textbox and click submit to get results.

   After clicking submit, you will see NER results and Parsed results. And you can click "back to form" at the bottom of the page to try other input sentences you want.

3. Streamlit application
   
   To start the Streamlit application, type below command in your terminal:
   
   ```
   $ streamlit run app_streamlit.py
   ```
   You can access the application at http://localhost:8501/.
   
   The application has a sidebar where you can select a task. If you selected Named Entity Recognition, you can type your input in textbox and it will show the result of spaCy NER in a table and a bar chart of word frequencies. If you select Dpendency Parsing, it will show the result of the dependency parser for each input sentence in two visualization options: Table or Graph.