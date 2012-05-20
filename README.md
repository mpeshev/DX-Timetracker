DX-Timetracker
==============

Small timetracking script in Python - run it with:

python timetracker.py PROJECTNAMEHERE

And if the project exists, it shall be reused. Otherwise a new project would be created.

The timetracking is running until you type 'stop' in the terminal where the file is populated and the database as well.

Use sqlite to query and select reports on projects, such as:

sqlite> select strftime('%M', end) - strftime('%M', start) from timings;