import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

createCourses = "CREATE TABLE coursesT(code TEXT, mark INTEGER, id INTEGER);"
createPeople = "CREATE TABLE peepsT(name TEXT, age INTEGER, id INTEGER);"

c.execute(createCourses)
c.execute(createPeople)

courses = csv.DictReader(open("data/courses.csv"))
people = csv.DictReader(open("data/people.csv"))

for row in courses:
    c.execute("INSERT INTO coursesTable VALUES (?,?,?);", (row['code'], int(row['mark']), int(row['id'])))
for row in people:
    c.execute("INSERT INTO peepsTable VALUES (?,?,?);", (row['name'], int(row['age']), int(row['id'])))
#command = ""          #put SQL statement in this string
#c.execute(command)    #run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database
