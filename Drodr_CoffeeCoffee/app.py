# app.py

from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Sample data for menu items and categories
menu_data = [
    {
        'name': 'Espresso',
        'items': [
            {'id': 1, 'name': 'Espresso Shot', 'price': 2.99},
            {'id': 2, 'name': 'Caffe Americano', 'price': 3.99},
            # Add more espresso items here...
        ]
    },
    {
        'name': 'Cappuccino',
        'items': [
            {'id': 3, 'name': 'Classic Cappuccino', 'price': 4.99},
            {'id': 4, 'name': 'Vanilla Cappuccino', 'price': 5.99},
            # Add more cappuccino items here...
        ]
    },
    # Add more categories here...
]

# Sample data for the cart
cart = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', menu_data=menu_data)
@app.context_processor
def calculate_total_price():
    def calculateTotalPrice():
        total_price = 0
        for item in cart:
            total_price += item['price'] * item['quantity']
        return total_price
    return dict(calculateTotalPrice=calculateTotalPrice)
@app.route('/cart')
def show_cart():
    return render_template('cart.html', cart=cart)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item_id = int(request.json['item_id'])
    item_quantity = int(request.json['item_quantity'])
    
    # Find the item in the menu based on its ID
    for category in menu_data:
        for item in category['items']:
            if item['id'] == item_id:
                cart_item = {
                    'id': item['id'],
                    'name': item['name'],
                    'price': item['price'],
                    'quantity': item_quantity
                }
                cart.append(cart_item)
                return jsonify({'message': 'Item added to cart'})

    return jsonify({'message': 'Failed to add item to cart'})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process the login form data
        # ...
        return redirect(url_for('index'))  # Replace 'index' with the appropriate endpoint for the home page

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Process the signup form data
        # ...
        return redirect(url_for('index'))  # Replace 'index' with the appropriate endpoint for the home page

    return render_template('signup.html')

@app.route('/place_order', methods=['GET', 'POST'])
def place_order():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        customer_address = request.form['customer_address']
        
        # Process the order and perform necessary actions
        
        # Clear the cart
        cart.clear()
        
        return redirect(url_for('thank_you'))
    
    return render_template('place_order.html', cart=cart)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
