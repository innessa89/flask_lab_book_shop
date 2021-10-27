from flask import render_template 
from app import app
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html',title="Book Shop",orders=orders)

@app.route('/orders/<order_number>')
def order(order_number):
    return render_template('ordernumber.html',title=order_number,order=orders[int(order_number)-1])