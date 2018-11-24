# flask.lawrencemcdaniel.com


## Resources
Zappa setup: https://blog.apcelent.com/deploy-flask-aws-lambda.html
Flask: http://flask.pocoo.org/
SQLAlchemy: https://www.sqlalchemy.org/
# flask.lawrencemcdaniel.com


## Local dev environment setup
1. AWS Credentials
2. pip install awscli
3. Create Virtual Environment
  a. cd to the local git repository
  b. virtualenv -p python3 env3
  c. source .env3/bin/activate
  d. pip install -r requirements.txt
  e. zappa init

4. Run Flask web server:
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
5. Deploy app to AWS: zappa deploy dev
6. Subsequent app updates to aws: zappa update dev
