from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    restaurantpizzas = db.relationship('Restaurant_Pizzas', backref='restaurant')


class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    name=  db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at=  db.Column(db.DateTime(), default=db.func.now())
    updated_at=  db.Column(db.DateTime(), onupdate=db.func.now())

    restaurantpizzas = db.relationship('Restaurant_Pizzas', backref='pizza')    

class Restaurant_Pizzas(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzass'
    id = db.Column(db.Integer, primary_key=True)
    price=  db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

