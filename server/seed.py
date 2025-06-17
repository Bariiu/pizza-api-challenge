from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    print("Seeding data...")

    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    r1 = Restaurant(name="Akoth's Kitchen", address="Kenyatta Avenue")
    r2 = Restaurant(name="Chebet's CheeseNdom", address="Moi Avenue")

    p1 = Pizza(name="Margherita", ingredients="cheese, tomato sauce, basil")
    p2 = Pizza(name="BBQ Chicken", ingredients="bbq sauce, chicken, onions")
    p3 = Pizza(name="Veggie Delight", ingredients="peppers, mushrooms, olives")

    rp1 = RestaurantPizza(price=850, pizza=p1, restaurant=r1)
    rp2 = RestaurantPizza(price=950, pizza=p2, restaurant=r1)
    rp3 = RestaurantPizza(price=700, pizza=p3, restaurant=r2)

    db.session.add_all([r1, r2, p1, p2, p3, rp1, rp2, rp3])
    db.session.commit()

    print("Done seeding!")
