## Setup
- Install [Python](https://www.python.org/downloads/)
- Install [PostgreSQL](https://www.postgresql.org/download/)
- Setup [venv](https://docs.python.org/3/library/venv.html)
	- Recommended: create in source directory -> `/backend`
- Install dependencies
	- `> pip install -r requirements.txt`
- Install [pgAdmin4](https://www.pgadmin.org/download/)
- [Create pg server & database](https://www.tutorialsteacher.com/postgresql/connect-to-postgresql-database)
	- Remember user & password!!!
- Create .env file in `/Courses/Courses` directory
	- Keys to include:
		`DB_NAME=<db_name>`
		`DB_USER=<db_user>`
		`DB_PASSWORD=<db_user_password>`
		`DB_HOST=<db_host> ('localhost' if testing locally)`
		`DB_PORT=<db_port>`
- Create and run db migrations:
	- Head to `/Courses/Courses`
	- Execute:
	`> python manage.py makemigrations`
	`> python manage.py migrate`
	
## Run
#### Start virtual enviroment
Head to `/venv/Scripts` and execute `activate script`.
Example:

    > cd /venv/Scripts
    > ./activate

#### Run Server
With virtual enviroment activated, head to folder `/backend/Courses` and execute `python manage.py runserver`

> Note: If you're using windows, execute `/Courses/start_server.ps1` file in powershell and setup & run will be executed automatically if the suggested project structure has been followed.