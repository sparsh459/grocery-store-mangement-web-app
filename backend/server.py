from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import productdao
import umdao
import json
import ordersdao

# creating a flask app
app = Flask(__name__)
connection = get_sql_connection()


# this /getproducts is an entry point for the website
# putting getallproducts API from productdao in this server file
@app.route('/getproducts', methods=['GET'])
def getproducts():
    products = productdao.getallproducts(connection)
    # jsonify() is a helper method provided by Flask to properly return JSON data.
    response = jsonify(products)
    # we put this access control so that frontend can call backend
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/um_dao', methods=['GET'])
def um_dao():
    response = umdao.getum(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# inserting order and it's details in database
# and it is very similar to the inserting products in database
@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = ordersdao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# inserting products in database
@app.route('/insertProduct', methods=['POST'])
def insert_product():
    # getting data from frintend to backend through ""request_payload""
    # input that we get from UI is in immutable dict which is tehn converted to string in js file and then send that
    # json string to backend which is teh n converted to a dictionary for python to read
    request_payload = json.loads(request.form['data'])
    product_id = productdao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = productdao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# get list on all orders to teh UI, displaying it
@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = ordersdao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)
