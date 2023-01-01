# People_Database

There is a simple database of people that can look like this (CSV format):

- id,name,birth_date,father_id,mother_id
- 1,Jan Kowalski,1960-06-01,,
- 2,Anna Wiśniewska,1962-01-06,,
- 3,Adam Kowalski,1984-03-03,1,2

In Person class single person is created using information given in database.
People can have children, mothers, fathers etc. They are unique using ids, names and birth dates.

My programme creates database class with list of people (instances of Person classes).
Database class is creating a dictionary of people with ids as keys. You can additionaly:
- add single person to the database 
- get person by it's id 
- "calculate" family tree of the person by it's id

Database_IO can write and read databases to and from CSV files. 
It can additionaly create family tree and generate it into YAML file.
