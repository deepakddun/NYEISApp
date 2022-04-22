from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging as logger
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.secret_key = '543af292a648479e77c6b86b13b95179209f77c13bee75ff916d4f888418b09b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://demo_user:Password123@localhost:3306/sample_db'
db = SQLAlchemy(app)

# Routes
from NYEIS_Site import routes