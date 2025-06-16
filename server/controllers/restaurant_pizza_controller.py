from flask import Blueprint, request, jsonify
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from server.app import db

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('/', methods=['POST'])
def add_pizza_to_restaurant():
    data = request.get_json()

    try:
        price = int(data.get('price'))
        if not (1 <= price <= 30):
            return jsonify({'errors': ['Price must be between 1 and 30']}), 400
    except (ValueError, TypeError):
        return jsonify({'errors': ['Invalid price value']}), 400

    new_entry = RestaurantPizza(
        price=price,
        pizza_id=data.get('pizza_id'),
        restaurant_id=data.get('restaurant_id')
    )

    db.session.add(new_entry)
    db.session.commit()

    pizza = Pizza.query.get(data.get('pizza_id'))
    return jsonify({
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    }), 201
