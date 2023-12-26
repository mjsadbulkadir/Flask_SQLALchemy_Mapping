from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

user_channel = db.Table('user_channel', 
                        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                        db.Column('channel_id', db.Integer, db.ForeignKey('channel.id')))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    following = db.relationship('Channel', secondary=user_channel, backref='channels')
    
    def __repr__(self):
        return f'<user: {self.name}>'
    
class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<channel: {self.name}>'
    
if __name__ == "__main__":
    app.run(debug=True, port=8000, use_reloader=False)
