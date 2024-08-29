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

## Introduction:
My Project was a long time process to find what i want to do and what i can do with my skills beside my work.
I am working as an Software Engineer but in a different Segment, i work mainly in the API Section and didn't had any contact with Web Development yet. 

This project was very interesting for me because i can now develop my skills further in the section i want to go and thats Fullstack (main Backend)

## Project Structur:
#### Programming Language
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


## DB
#### Schema.sql
In the schema.sql are the tables and their structure and how the are interpreted. 
In my case there are three tables displayed: personal_data, work_experience, skills

This includes the most changeable data in my portfolio at the moment, thats why i took these tables for the application. 
Things like experience and school tends not to change.

#### init_db
the init DB is the file that needs to be run by python to create the Database File
to get more out of the file than just creating the database file and the tables in it.
I implemented the prefill for my existing data with insert commands for all tables. 

after the inserts are executed the database connection gets commited and with the commit the data is saved in the db file. 
for resource and security reasons the db connection is closed. 


## Static
in the static folder all fixed assets are placed. 
This includes some placeholder but the folder structure i found the most applicable is:
- css
- icons
- img
- js

## css
the css i split in three files
- sidebar 
- styles
- top
The Styles is the main css and the other two are created afterwards for my own overview
i have created my own css files with some help from inspirations i found for my portfolio.

#### js
The JS animates the switch on the top of the side.
Which switches between the words : Websites,Apps,Databases, your projects

## App.py
In the App.py the connection to the database is established and the information form the tables are extracted to work with them in the flask html files. 
The reason its a one pager the app.py only has one route. 

The App.py loads the render_template and calls the "index.html"

## Index.html
The index.html is the main html site and controls all structure in this project. 

#### Navbar
The Navigationbar is responsive and fixed on top of the page even when its scrolling

#### Include Header
The Header has all the information on the first page in its.
The structure i build for a clean look and direct view on the important with a good readable text.
#### Include about
the about section is my favorite because the programming like style i created looks pretty good to me. 
Even if its programming style normal people can still understand the important points fast.
I did most of the points with css to create this look.

This is the only section that uses the flask placeholder to get the information form the database
But most of the code is replaced with the flask and not repeated programmed like in the first place as i created this website only with html

#### Include work
the include works needs more work i have done beside my regular work but will be extended one i completed more projects

#### Include contact
the contact form includes all ways people can contact me


## Future
The future for this project will be more optimization with the coding and including a way or a seperate program to fill the Database. 
I plan to expand the Database and the features of the Website in the future

## Thank you
a big thank you for this opportunity to show the world what i can do

