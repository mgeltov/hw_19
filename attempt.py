import base64

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from dao.model.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///./movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db = SQLAlchemy(app)

with db.session.begin():
    user = db.session.query(User).get(1)

# for user in all_users:
    # user_pass = base64.b64decode(user.password)
print(base64.b64decode(user.password))