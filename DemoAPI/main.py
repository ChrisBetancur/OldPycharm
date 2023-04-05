from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

'''class Drink(db.Model):
    def __init__(self):
        self.id = db.Column(db.Integer, primary_key=True)
        self.name = db.Column(db.String(80), unique=True, nullable=False)
        self.description = db.Column(db.String(120))

    def get_map(self):
        return {"name": self.name, "id": self.id, "description": self.description}

    def __repr__(self):
        return f"{self.name} - {self.description}"'''


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def get_map(self):
        return {"name": self.name, "id": self.id, "description": self.description}

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route("/delete", methods=['DELETE'])
def test():
    delete = Drink.query.all()
    db.session.delete(delete)
    db.session.commit()
    return "Delete"


@app.route('/drinks/<name>', methods=['GET'])
def get_drink(name):
    drinks = Drink.query.all()

    output = []

    for drink in drinks:
        if drink.name == name:
            drink_data = {'name': drink.name, 'description': drink.description}
            output.append(drink.__repr__())
        # output.append(drink.get_map())
    print(output)
    return {"drinks": output}


@app.route('/drinks/getAll', methods=['GET'])
def get_drinks():
    drinks = Drink.query.all()

    output = []

    for drink in drinks:
        drink_data = {'id': drink.id, 'name': drink.name, 'description': drink.description}
        output.append(drink_data)
        # output.append(drink.get_map())
    print(output)
    return {"drinks": output}


@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}


@app.route('/drinks/<int:id>', methods=['GET'])
def get_drink_by_id(id):
    drink = Drink.query.get_or_404(id)
    return {'name': drink.name}


@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):

    drink = Drink.query.get(id)
    if drink is None:
        return {"Error": "Id not found"}

    db.session.delete(drink)
    db.session.commit()
    return {"Status": id}


if __name__ == '__main__':
    app.debug = True
    app.run()
