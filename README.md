# fit

## start project 

with docker:
`docker-compose --profile main up`

manually:
  frontend:
    `npm install`
    `npm run serve`
  
  backend:
    `python -m venv venv`
    Windows
    `venv\Script\active`
    Linux and MacOS:
    `source venv/bin/activate`

    `pip install -r requirements.txt`
    `python manage.py migrate`
    `python manage.py createsuperuser`
    `python manage.py runserver`
  

start mailhog locally:
`docker-compose --profile mailhog-only up`
