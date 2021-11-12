from sql_connection import get_sql_connection


def getum(connection):
    cursor = connection.cursor()
    # query to access the unit management database in the mysql
    query = "SELECT * FROM grocerydb.uom;"
    cursor.execute(query)
    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response


if __name__ == '__main__':
    # calling to database from sql_connection.py
    connection = get_sql_connection()
    print(getum(connection))
