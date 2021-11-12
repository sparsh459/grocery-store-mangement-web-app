# dao = data access object
from sql_connection import get_sql_connection


# functon to get all the data regarding products from database
def getallproducts(connection):
    # creating the curser object to execute the query and fetch the records from the database
    cursor = connection.cursor()
    # query for what we want from our database
    query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, "
             "uom.uom_name FROM grocerydb.products inner join uom on products.uom_id = "
             "uom.uom_id ")
    # executing SQL statement abouve in a way in which python connects from database
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'unit_name': uom_name
        })

    connection.close()
    return response


# function to insert in data base
def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    # commit helps to permanently submit in database
    connection.commit()
    # below will tell the id of the last row that is currently inserted
    return cursor.lastrowid


# function to delete in database
def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return 'Deleted'


if __name__ == '__main__':
    # calling to database from sql_connection.py
    connection = get_sql_connection()

    # print(getallproducts(connection))

    # print(insert_new_product(connection, {
    #     'product_name': 'Ghee',
    #     'uom_id': '3',
    #     'price_per_unit': 90
    # }))

    # print(delete_product(connection, 14))
