from sys import argv
import datetime
import sqlite3

# init DB connection
conn = sqlite3.connect('timetrack.db')
c = conn.cursor()

# get variables
script, project = argv
start = datetime.datetime.now()
start_datetime = start.strftime("%Y-%m-%d %H:%M:%S")
filename = "records.log"

# open filename
c.execute("SELECT id FROM projects WHERE name = ?", (project, ))
data = c.fetchone()

if data is None:
	c.execute("INSERT INTO projects(name) VALUES(?)", (project, ))
	c.execute("select last_insert_rowid()")
	data = c.fetchone()

project_id = data[0]

target = open(filename, 'a')

print "Project %r started" % project

# write start
target.write("%r started on: %r" % ( project, start.strftime("%Y-%m-%d %H:%M:%S") ) )
target.write("\n")
target.flush()

# wait for stop
print "Type 'stop' to close a project"

entry = raw_input()
while not entry == 'stop':
	entry = raw_input()
	
# write ends
end = datetime.datetime.now()
end_datetime = end.strftime("%Y-%m-%d %H:%M:%S")

target.write("%r ended on: %r" % ( project, end.strftime("%Y-%m-%d %H:%M:%S") ) )
target.write("\n\n")


# insert into DB
c.execute("INSERT INTO timings(start, end, project_id) VALUES(?, ?, ?)", (start_datetime, end_datetime, project_id,))

conn.commit()

print start
print end

c.close()
target.close()
