from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db=SQLAlchemy(app)

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    address = db.Column(db.String(100))
    workers = db.relationship('Worker', backref = 'owner') 

class Worker(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id', ondelete = 'CASCADE'))
    
with app.app_context():
     db.create_all()

if __name__ == "__main__":
     app.run(debug=True,port=8000,use_reloader = False)
    