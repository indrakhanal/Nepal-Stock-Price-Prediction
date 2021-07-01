from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class StockScript(db.Model):
    __tablename__ = 'script_info'

    id = db.Column(db.Integer, primary_key=True)
    script_name = db.Column(db.String())

    def __init__(self, script_name):
        self.script_name = script_name

    def __repr__(self):
        return f"{self.script_name}"
