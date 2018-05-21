from flask import Flask
#import mysql.connector

from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

app.secret_key = 'some$3cretKey'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'shhsjcava'
#app.config['MYSQL_USER'] = 'davab'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB'] = 'go_peli'
from app import views



# from mysql.connector import (connection);

# cnx = connection.MySQLConnection(user='*******', password='********',
#                                  host='*.*.*.*',
#                                  database='database_name')
# cnx.close()