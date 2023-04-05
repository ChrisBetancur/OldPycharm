from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Drink(db.Model):
    def __init__(self):
        self.id = db.Column(db.Integer, primary_key=True)
        self.name = db.Column(db.String(80), unique=True, nullable=False)
        self.description = db.Column(db.String(120))

    def get_map(self):
        return {"name": self.name, "id": self.id, "description": self.description}

    def __repr__(self):
        return f"{self.name} - {self.description}"


# db.create_all()
# db.session.add(name="Cherry", description="Bruh")

drink = Drink(name="Grape", description="Bruh")
print(drink)


@app.route('/')
def index():
    return 'Hello'


'''@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()

    output = []

    for drink in drinks:
        output.append(drink.get_map())

    return {"drinks": output}'''
