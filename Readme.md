CS50 - Final Project - Portfolio Website
#### Video Demo:  https://youtu.be/FcCnndsKDw0
#### Description:
Portfolio Website for my own with Python and Web Development
Techstack: 
Flask
Python
Html
CSS
JScript
SQLite

#### Introduction:
My Project was a long time process to find what i want to do and what i can do with my skills beside my work.
I am working as an Software Engineer but in a different Segment, i work mainly in the API Section and didn't had any contact with Web Development yet. 

This project was very interesting for me because i can now develop my skills further in the section i want to go and thats Fullstack (main Backend)

#### Project Structur:
## Programming Language
i chose Web development and Python because i didn't hat much contact with it in my past and want to improve in this area. 
Flask was an good way to fulfil my needs for this project

The Mainfolder of the project are:

- DB
    - Includes all Database relative Files
- static
    - includes all Assets and not changed files
- templates
    - includes all structural and content files
    - like html files and there relation to each other.
- app.py
    - this is the entry point of the program and builds up the application.


#### DB
## Schema.sql
In the schema.sql are the tables and their structure and how the are interpreted. 
In my case there are three tables displayed: personal_data, work_experience, skills

This includes the most changeable data in my portfolio at the moment, thats why i took these tables for the application. 
Things like experience and school tends not to change.

## init_db
the init DB is the file that needs to be run by python to create the Database File
to get more out of the file than just creating the database file and the tables in it.
I implemented the prefill for my existing data with insert commands for all tables. 

after the inserts are executed the database connection gets commited and with the commit the data is saved in the db file. 
for resource and security reasons the db connection is closed. 


#### Static
in the static folder all fixed assets are placed. 
This includes some placeholder but the folder structure i found the most applicable is:
- css
- icons
- img
- js

## css
i have created my own css files with some help from inspirations i found for my portfolio.

