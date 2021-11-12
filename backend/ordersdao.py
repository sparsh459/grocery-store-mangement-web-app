from sql_connection import get_sql_connection
from datetime import datetime


# insert order functionthat takes connection and order as a dictionary
def insert_order(connection, order):
    cursor = connection.cursor()

    # current query is to insert in order table in database
    # insert order
    order_query = ("INSERT INTO orders "
                   "(customer_name, total, datetime)"
                   "VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['grand_total'], datetime.now())

    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    # insert order details
    order_details_query = ("INSERT INTO order_details "
                           "(order_id, product_id, quantity, total_price)"
                           "VALUES (%s, %s, %s, %s)")
    # since we're inserting multiple details
    order_details_data = []
    # for iterating order details dict inside the input
    for order_detail_record in order['order_details']:
        order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])

    # for inserting multiple details in database
    # since we're passing multiple records, we're passing an array named order_details_data
    cursor.executemany(order_details_query, order_details_data)
    connection.commit()

    return order_id


def get_all_orders(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM grocerydb.orders;"
    cursor.execute(query)

    # putting all the orders in a list with dict type element inside it
    response = []
    for (order_id, customer_name, total, dt) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': total,
            'datetime': dt,
        })

    # cursor.close()
    #
    # # append order details in each order
    # for record in response:
    #     record['order_details'] = get_order_details(connection, record['order_id'])

    return response


if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders(connection))
    # print(insert_order(connection, {
    #     'customer_name': 'hamid',
    #     'grand_total': '500',
    #     # 'datetime': datetime.now(),
    #     'order_details': [
    #         {
    #             'product_id': 1,
    #             'quantity': 2,
    #             'total_price': 50
    #         },
    #         {
    #             'product_id': 3,
    #             'quantity': 1,
    #             'total_price': 30
    #         }
    #     ]
    # }))
