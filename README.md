<h1 style="text-align: center">welcome to dashboard django project</h1>
<h2>this is a django project. this project refer a simple sample dashboard</h2>

## Main tools used in this project:

- python: 3.12.8
- django: 4.12.7
- mysql:  9.1.0


## packages

<i>packages used in this project are in the <b>"requirements.txt"</b> in root of project</i>

## Database

- database is in the <b>"database"</b> folder
- db name:    dashboard
- mysql host: localhost
- mysql port: 3306
- username:   amirhossein
- password:   "efkwjh3984rh(ORHFIL&ET@*G@Y$^*&@QYHGOI*"


## How to run the project

- clone the project
- you must run all command in root of project
- run these commands:
```bash
  python -m venv .venv
  .venv/scripts/activate
  python -m pip install -r requirements.txt
```
- import the <b><i>dashboard</i></b> db with utf8 charset in your mysql
- you must configure your mysql with user account that specified in database section, or you can change the settings file with your favorite user account
- finally, run this command and browse to showed link
```bash
  python manage.py runserver
```
## DB Admin
- if you want use the default admin section for working on database, do these steps:
- run this command:
```bash
python manage.py createsuperuser
```
- after you created a super user for admin, you can use it in below address:
```bash
localhost:yourlocalport/admin
```
