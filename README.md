# flask-lambda-api

This is serverless/restful API built using Flask.

## Running scheme

1. py -3 -m venv env
2. env\scripts\activate
3. pip install flask
4. set FLASK_APP=app.py
5. set FLASK_ENV=development
6. flask run

## Deployment

0. Configure AWS-CLI ["https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html"]
1. pip install zappa
2. zappa deploy dev
3. zappa update dev
