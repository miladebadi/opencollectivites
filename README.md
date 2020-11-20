# Open Collectivités

![Open Collectivités](open-collectivites.png?raw=true "Open Collectivités")


Simplifier l’accès aux informations financières et statistiques des collectivités locales

[Page de présentation du défi](https://entrepreneur-interet-general.etalab.gouv.fr/defis/2020/open-collectivites.html)

## Install
### Packages
- `sudo apt install python3-dev python3-venv postgresql libpq-dev`

### Prepare database
- Create a PostgreSQL database and user
```
sudo -u postgres psql
postgres=# CREATE DATABASE opencollectivites;
postgres=# CREATE USER opencollectivites WITH ENCRYPTED PASSWORD 'your_password';
postgres=# GRANT ALL PRIVILEGES ON DATABASE opencollectivites TO opencollectivites;
```

- Create the Unaccent extension manually

```
postgres=# CREATE EXTENSION unaccent;
```

### Install the project
#### Clone the project and get the submodules
- `git clone` this repository somewhere and `cd` in.
- `git submodule init`
- `git submodule update`

#### Initiate local settings
- `cp settings_local.py.sample settings_local.py`
- Fill the `settings_local.py` file

#### Create and activate the virtualenv
- `python3 -m venv venv`
- `source venv/bin/activate`

#### Install the Python dependancies 
- `pip install wheel`
- `pip install -r requirements.txt`

#### Initiate the database and static files for Django
- `python3 manage.py migrate`
- `python3 manage.py collectstatic`

#### Create the superuser
- ` python manage.py createsuperuser`

### Launch it
 - `python3 manage.py runserver`
