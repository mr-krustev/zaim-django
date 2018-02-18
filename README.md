# zaim-django

<< PROJECT DESCRIPTION >>

## Set-Up

## MySQL

1. Install the MySQL server and Shell and preferably MySQL Workbench.
2. Create mysql_db.conf file in the zaim root directory. It should have this format:
```
[client]
database = <DB_NAME>
host = localhost
user = <DB_USER>
password = <DB_USER_PASSWORD>
default-character-set = utf8
```
2. Create DB(schema in workbench). I.e.: zaim-django.
3. Create a user with DB-Manager role and also add REFERENCES privilege.
4. Replace DB_NAME with the new schema name, DB_USER with the user you created and his password.

### Dependencies

1. Run `mkvirtualenv zaim-django`. This will create a virtual python environment with the name zaim-django.
2. Run `pip install -r requirements.txt` in the zaim folder. This will install all dependencies defined in the requirements.txt file.
Note: You might need to provide the path unless you run the command from the zaim folder.
3. Run `python manage.py makemigrations` in the zaim root directory. This will generate the SQL migrations in their respective folders.
4. Run `python manage.py migrate` in the zaim root directory. This will run the migrations generated in step 3 and perform the SQL query in the DB.
5. Run `python manage.py runserver` in the zaim root directory to start the server.


