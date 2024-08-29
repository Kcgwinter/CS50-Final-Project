import sqlite3
connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

    cur = connection.cursor()
    print("connection open")
    cur.execute("INSERT INTO personal_data (name, dayOfBirth, email) VALUES ('Kevin Christopher George Winter', '03/06/1992', 'kcgwinter@gmail.com')")
    
    cur.execute("INSERT INTO work_experience (title, fromTill, city, company) VALUES ( ?, ? ,?, ?)",
                ('Software Engineer', '06/2019 - Current', 'Cuxhaven, Germany', 'City of Cuxhaven'))
    cur.execute("INSERT INTO work_experience (title, fromTill, city, company) VALUES ( ?, ? ,?, ?)",
                ('Software Developer', '08/2017 - 06/2019', 'Cuxhaven, Germany', 'Voco GmbH'))
    cur.execute("INSERT INTO work_experience (title, fromTill, city, company) VALUES ( ?, ? ,?, ?)",
                ('Software Developer', '07/2015 - 07/2017', 'Bremen, Germany', 'Merentis GmbH'))


    cur.execute("INSERT INTO skills (title, years) VALUES ( ?, ?)",
                ("Languages:'C#','Python','PHP','HTML/CSS/JS','Powershell'", "9 Years"))
    cur.execute("INSERT INTO skills (title, years) VALUES ( ?, ?)",
                ("Frameworks: '.Net','Flutter', 'Laravel'", "9 Years"))
    cur.execute("INSERT INTO skills (title, years) VALUES ( ?, ?)",
                ("Database: 'MSSQL','MYSQL','Firebase'", "9 Years"))
    cur.execute("INSERT INTO skills (title, years) VALUES ( ?, ?)",
                ("Tools: 'GIT','SSMS','Kofax','ENAIO DMS', 'Figma'", "9 Years"))
    cur.execute("INSERT INTO skills (title, years) VALUES ( ?, ?)",
                ("Methodologies: OOP, Scrum", "9 Years"))
    cur.execute("INSERT INTO skills (title, years) VALUES ( ?, ?)",
                ("API Development, Frontend Development, Backend Development, Full-Stack Applications", "9 Years"))
    cur.execute("INSERT INTO skills (title, years) VALUES ( ?, ?)",
                ("English, German - All professional proficiency or above", "9 Years"))
    
    connection.commit()
connection.close()