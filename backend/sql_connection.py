import mysql.connector

__cnx = None


def get_sql_connection():
    print("Opening mysql connection")
    global __cnx
    # connecting to my sql databaes
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='root',
                                        host='127.0.0.1',
                                        database='grocerydb')
    return __cnx
