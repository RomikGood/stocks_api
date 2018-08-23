## Stocks API
==========

Author: `Roman Kireev'
Version: 1.0.0

## Getting Started
---------------

- Change directory into your newly created project.
    cd stocks_api
- Create a Python virtual environment.
    python3 -m venv env
- Upgrade packaging tools.
    env/bin/pip install --upgrade pip setuptools
- Install the project in editable mode with its testing requirements.
    env/bin/pip install -e ".[testing]"
- Configure the database.
    env/bin/initialize_stocks_api_db development.ini
- Run your project's tests.
    env/bin/pytest
- Run your project.
    env/bin/pserve development.ini

## Tools
Writtin with Python version 3.6/3.7.
</br>
Utilizied libraries:
- Pyramid
- Requests
- HTTPie
- Pytest
- OS

## Change Logs
- [x] `GET / `- returns a valid message response with directions

- [x] `GET /api/v1/stocks` - returns a correct message response from view function
- [x] `POST /api/v1/stocks` - returns a correct message response from view function