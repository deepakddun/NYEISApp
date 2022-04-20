from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '543af292a648479e77c6b86b13b95179209f77c13bee75ff916d4f888418b09b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://demo_user:Password123@localhost:3306/sample_db'
db = SQLAlchemy(app)

# Routes
from NYEIS_Site import routes