# ONLINE FOOD DELIVERY KNOWLEDGE REPOSITORY

# Food Items
food_items = {
    "F101": {
        "name": "Paneer Biryani",
        "category": "Main Course",
        "price": 250,
        "availability": 5
    },

    "F102": {
        "name": "Veg Burger",
        "category": "Fast Food",
        "price": 150,
        "availability": 25
    }
}


# Restaurants
restaurants = {
    "R101": {
        "name": "Spice Hub",
        "cuisine": "Indian",
        "location": "Delhi",
        "rating": 4.5
    },

    "R102": {
        "name": "Food Corner",
        "cuisine": "Fast Food",
        "location": "Delhi",
        "rating": 4.2
    }
}


# Customers
customers = {
    "C101": {
        "name": "Anusha",
        "location": "Delhi",
        "membership": "Premium"
    },

    "C102": {
        "name": "Riya",
        "location": "Delhi",
        "membership": "Regular"
    }
}


# Orders
orders = {
    "O101": {
        "customer": "C101",
        "restaurant": "R101",
        "food": "F101",
        "quantity": 6,
        "amount": 1500,
        "payment": "Successful",
        "status": "Delivered"
    },

    "O102": {
        "customer": "C102",
        "restaurant": "R102",
        "food": "F102",
        "quantity": 2,
        "amount": 300,
        "payment": "Failed",
        "status": "Pending"
    }
}


# Business Rule Processing
def apply_rules():

    print("ONLINE FOOD DELIVERY KNOWLEDGE REPOSITORY")
    print("------------------------------------------")

    for order_id, order in orders.items():

        print("\nOrder ID:", order_id)

        # Get related information
        food = food_items[order["food"]]
        customer = customers[order["customer"]]
        restaurant = restaurants[order["restaurant"]]

        # Rule 1: Low Food Availability
        if food["availability"] < 10:
            print("Decision: Low Availability Alert")

        # Rule 2: Premium Customer
        if customer["membership"] == "Premium" and order["amount"] > 500:
            print("Decision: Free Delivery")

        # Rule 3: Failed Payment
        if order["payment"] == "Failed":
            print("Decision: Payment Pending")

        # Rule 4: Delivered Order
        if order["status"] == "Delivered":
            print("Decision: Order Successfully Delivered")

        # Rule 5: High-Value Order
        if order["amount"] > 1000:
            print("Decision: Priority Order")

        # Rule 6: Highly Rated Restaurant
        if restaurant["rating"] >= 4.5:
            print("Decision: Recommended Restaurant")

        # Rule 7: Large Quantity Order
        if order["quantity"] >= 5:
            print("Decision: Large Order Alert")


# Run the knowledge repository
apply_rules()
