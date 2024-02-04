#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Restaurant, Pizza, Restaurant_Pizzas

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api= Api(app)
migrate = Migrate(app, db)

db.init_app(app)

class Index(Resource):
    def index(self):
        return "Index for Restaurant/Pizza API"

api.add_resource(Index, '/')


class RestaurantData(Resource): 
    def get(self):
        all_restaurants= Restaurant.query.all()
        restaurant_dict= [restaurant.to_dict() for restaurant in all_restaurants]
        response= make_response(jsonify(restaurant_dict), 200)
        return response

api.add_resource(RestaurantData, '/restaurants')

class RestaurantByID(Resource):
    def get_restaurant_by_id(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        restaurant_dict = restaurant.to_dict()

        response = make_response(
            jsonify(restaurant_dict),
            200
        )
        return response 

api.add_resource(RestaurantByID, '/restaurants/<int:id>')

class DeleteRestaurantByID(Resource):
    def delete_restaurant_by_id(self):
        restaurant = Restaurant.query.filter_by(id=id).first()
        db.session.delete(restaurant)
        db.session.commit()

api.add_resource(DeleteRestaurantByID, "/restaurants/<int:id>'", methods=["DELETE"])

class PizzaData(Resource):
    def get_pizzas(self):
        all_pizzas = Pizza.query.all()

        pizza_dict= [pizza.to_dict() for pizza in all_pizzas]

        response = make_response(
            jsonify(pizza_dict),
            200
        )
        return response 

api.add_resource(PizzaData,'/pizzas')




class RestaurantPizzas(Resource):
    def post_restaurant_pizzas(self):
        new_restaurant_pizza = HeroPower(
                price=request.form.get("price"),
                pizza_id=request.form.get("pizza_id"),
                restaurant_id=request.form.get("restaurant_id"),
            )

        db.session.add(new_restaurant_pizza)
        db.session.commit()

        restaurant_pizza_dict = new_restaurant_pizza.to_dict()

        response = make_response(
                jsonify(restaurant_pizza_dict),
                201
            )

        return response

api.add_resource(RestaurantPizzas, "/restaurant_pizzas", methods=["POST"])



if __name__ == '__main__':
    app.run(port=5555)
