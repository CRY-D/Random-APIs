from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    API = db.Column(db.String(255), nullable=False)
    Description = db.Column(db.String(500), nullable=False)
    Auth = db.Column(db.String(50), nullable=True)
    HTTPS = db.Column(db.Boolean, default=False)
    Cors = db.Column(db.String(50), nullable=True)
    Link = db.Column(db.String(255), nullable=False)
    Category = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<Entry {self.API}>'
