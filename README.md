# fit

## start project 

with docker:<br>
`docker-compose --profile main up`

manually:<br>
  frontend:<br>
    `npm install`<br>
    `npm run serve`
  
  backend:<br>
    `python -m venv venv`<br>
    Windows<br>
    `venv\Script\active`<br>
    Linux and MacOS:<br>
    `source venv/bin/activate`<br>

    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
  

start mailhog locally:<br>
`docker-compose --profile mailhog-only up`
