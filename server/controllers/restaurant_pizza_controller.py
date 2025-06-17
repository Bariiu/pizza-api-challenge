from flask import Blueprint, request, jsonify
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.app import db

restaurant_pizza_bp = Blueprint("restaurant_pizza_bp", __name__)

@restaurant_pizza_bp.route("/restaurant_pizzas", methods=["POST"])
def add_restaurant_pizza():
    data = request.get_json()

    try:
        price = int(data["price"])
        if price < 500 or price > 1000:
            return jsonify({"errors": ["Price must be between 500 and 1000"]}), 400

        new_rp = RestaurantPizza(
            price=price,
            pizza_id=data["pizza_id"],
            restaurant_id=data["restaurant_id"]
        )
        db.session.add(new_rp)
        db.session.commit()

        pizza = Pizza.query.get(data["pizza_id"])
        return jsonify({
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }), 201

    except (KeyError, TypeError, ValueError):
        return jsonify({"errors": ["Invalid data"]}), 400
