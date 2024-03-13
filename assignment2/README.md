# Assignment 2 - Flask SQLAlchemy

In this assignment, I hooked up my flask webserver in assignment 1 with a SQLite database using SQLAlchemy.

A. Required Python version: Python 3.11.7
B. Required Modules: 
```
spacy 3.7.2
Flask 2.2.5
Flask-SQLAlchemy 3.1.1
```
C. Run the Code:
    
To start the Flask webserver, navigate to folder assignment2 and run below command in terminal:

   ```
   $ python app_flask.py
   ```
   The webserver is now running on http://127.0.0.1:5000.

   Navigate to this browser, you can input whatever text you want in the textbox and click submit to get results.

   After clicking submit, you will see NER results and Parsed results. And you can click "back to form" at the bottom of the page to try other input sentences you want or click "go to database" to see entities and their relevant dependencies stored in database. There's also a clickable "back to form" at the bottom of database page where you can go to index page and enter sentences to submit again.
