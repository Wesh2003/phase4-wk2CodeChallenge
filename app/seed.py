from faker import Faker
from random import choice, randint

from app import app
from models import db, Restaurant, Pizza, Restaurant_Pizzas

# db.init_app(app)

fake = Faker()

with app.app_context():

    Restaurant.query.delete()
    Pizza.query.delete()
    Restaurant_Pizzas.query.delete()

    fake = Faker()


    for i in range(10):
        new_restaurant = Restaurant(name=fake.name(), address=fake.address())
        db.session.add(new_restaurant)
        db.session.commit()

    for i in range(10):
        pizza_name = ["Pastrami", "Haloumi", "Hawaian", "Meat Feast", "Veg Fever"]
        ingredient_name = ["Tomato", "Onions", "Mushrooms", "Cheese", "Pepper"]
        new_pizza = Pizza(name=choice(pizza_name), ingredients=choice(ingredient_name))
        db.session.add(new_pizza)
        db.session.commit()


    restau= Restaurant.query.all()
    pizz= Pizza.query.all()

    for i in range(10):
      rand_restaurant= choice(restau)
      rand_pizza= choice(pizz)

      new_restaurant_pizza= Restaurant_Pizzas(price= randint(1,30), restaurant_id= rand_restaurant.id,  pizza_id= rand_pizza.id)
      db.session.add(new_restaurant_pizza)
      db.session.commit()



