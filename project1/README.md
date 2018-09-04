# Project 1 - Read&Review

Harvard's CS50 - Web Programming with Python and JavaScript.  
Second project from cs50 course - book review website.

I've bent project's requirements a little bit. Yes, I' ve used ORM(but some things are done with pure SQL), because I am familiar with SQL and i want to lear Flask and its extensions more.   
Additional and not necessary library used for import script - psycopg2 it also used only for learning purpose :) 
  
#### How to run app:
Before run install all of the requirements.  
Provide environmental variables: goodread key (env: GOODREAD_KEY) and path to 
flask config (env: FLASK_CONFIG) with SECRET_KEY and SQLALCHEMY_DATABASE_URI

Example flask config:
```angular2html
>> cat config_file.cfg

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

DEBUG=True
SQLALCHEMY_DATABASE_URI='YOUR_URI'
SECRET_KEY='YOUR_KEY'
```
For import script create yaml file with keys: postgresql: {host, port, database, user, password}

###### Overview:
```angular2html
In this project, you’ll build a book review website. 
Users will be able to register for your website and then log in using their username and password.
Once they log in, they will be able to search for books, leave reviews for individual books, 
and see the reviews made by other people. You’ll also use the a third-party API by Goodreads,
another book review website, to pull in ratings from a broader audience. Finally,
users will be able to query for book details and book reviews programmatically via your website’s API.

More information at:
https://docs.cs50.net/web/2018/w/projects/1/project1.html
```