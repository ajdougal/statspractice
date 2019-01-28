import mysql.connector


def get_mysql_db_connector():
    host = "localhost"
    user = "root"
    passwd = "password"

    mydb = mysql.connector.connect(host=host, user=user, passwd=passwd)

    return mydb

