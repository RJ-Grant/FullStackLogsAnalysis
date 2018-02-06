This is a Catalog Report Website using Python, Psycopg2, and PostgreSQL

REQUIREMENTS:

This code requires the user to have Python on their computer. This website
project uses Python 2.7.13. You can download Python at the following link:
https://www.python.org/downloads/release/python-2713/

TO RUN THIS CODE AND DISPLAY THE WEBSITE

Before you run the program, there are two views that must be created. They are
listed below:

##this creates a view including dates and status of each request##
create view truncated_times as
select date_trunc('day', time) as time, status from log;

##this creates a view of each day and the total requests for that day##
create view requests as
select time, count(*) as total from truncated_times
group by time;

##this creates a view of each day and the number of error requests of that day##
create view ERR_status as
select time, count(*) as num from truncated_times
where status = '404 NOT FOUND'
group by time;

Once the views are loaded into the database, you can run this code
in a vagrant vm, command prompt, or terminal. Complete the following steps
to run the program:

1. Navigate to the catalog directory (where this README exists!)
2. Run the catalog.py file (python3 catalog.py)

Once the file is running, go to localhost:8000 in a web browser
