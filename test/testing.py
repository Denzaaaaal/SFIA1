from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os
import urllib3

app = Flask(__name__)

app.config["MYSQL_HOST"] = os.environ.get('MYSQLHOST')
app.config["MYSQL_USER"] = os.environ.get('MYSQLUSER')
app.config["MYSQL_PASSWORD"] = os.environ.get('MYSQLPASSWORD')
app.config["MYSQL_DB"]  = os.environ.get('MYSQLDB')

mysql = MySQL(app)

#Testing HTTP status for login page
def test_login():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.178.55:5000/')
    assert 200 == r.status

# Testing HTTP status for sign_up page
def test_sign_up():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.178.55:5000/sign_up')
    assert 200 == r.status

# Testing HTTP status for account_overview page
def test_account_overview():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.178.55:5000/account_overview')
    assert 200 == r.status

# Testing HTTP status for income_overview page
def test_income_overview():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.178.55:5000/income_overview')
    assert 200 == r.status

# Testing HTTP status for expense_overview page
def test_expense_overview():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.178.55:5000/expense_overview')
    assert 200 == r.status

# Testing HTTP status for investment_overview page
def test_investment_overview():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.178.55:5000/investment_overview')
    assert 200 == r.status

# Testing how many records are called for the expense table
def test_select():
    with app.app_context():
        cur = mysql_connection.cursor()
        num_of_records = cur.execute("select * from expense;")
        mysql.connection.commit()
        cur.close()
        assert 6 == num_of_records # How many records are you expecting to return

# Testing how many records are called for the income table
def test_select():
    with app.app_context():
        cur = mysql_connection.cursor()
        num_of_records = cur.execute("select * from income;")
        mysql.connection.commit()
        cur.close()
        assert 6 == num_of_records

# Testing how many records are called for the investment table
def test_select():
    with app.app_context():
        cur = mysql_connection.cursor()
        num_of_records = cur.execute("select * from investment;")
        mysql.connection.commit()
        cur.close()
        assert 6 == num_of_records