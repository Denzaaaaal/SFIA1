from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config["MYSQL_HOST"] = os.environ.get('MYSQLHOST')
app.config["MYSQL_USER"] = os.environ.get('MYSQLUSER')
app.config["MYSQL_PASSWORD"] = os.environ.get('MYSQLPASSWORD')
app.config["MYSQL_DB"]  = os.environ.get('MYSQLDB')

mysql = MySQL(app)

@app.route("/", methods = ['GET', 'POST']) # Authenicate password
def hello(): 
    if request.method == "POST":
        details = request.form
        Username = details['username']
        Password = details['passwd']
        cur = mysql.connection.cursor()
        cur.execute("select username, passwd from user_details where username= %s", (Username))
        mysql.connection.commit()
        rows = cur.fetchall()
        cur.close()
    return render_template("index.html", title = "YMOYL - Home Page")
 
@app.route("/sign_up", methods = ['GET','POST'])
def sign_up():
    rows = []
    if request.method == "POST":
        details = request.form
        Username = details['username']
        Password = details['passwd']
        First_Name = details['first_name']
        Last_Name = details['last_name']
        Date_Of_Birth = details['date_of_birth']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user_details (username, passwd, first_name, last_name, dob) VALUES (%s, %s, %s, %s, %s)", (Username, Password, First_Name, Last_Name, Date_Of_Birth))
        mysql.connection.commit()
        rows = cur.fetchall()
        cur.close()

    info = []

    for row in rows: 
        info.append(row)

    return render_template("sign_up.html", title = "YMOYL - Sign up", info1 = info)

@app.route("/account_overview")
def account_overview():
    cur = mysql.connection.cursor()
    cur.execute("select username from user_details")
    mysql.connection.commit()
    cur.close()
    tincome = 100
    texpense = 200
    tinvestment = 300
    return render_template("account_overview.html", title="YMOYL - Account Overview", tincome = tincome, texpense = texpense, tinvestment = tinvestment)

@app.route("/income_overview") 
def income_overview():
    cur = mysql.connection.cursor()
    cur.execute("select * from income")
    mysql.connection.commit()
    rows =  cur.fetchall()
    cur.close()

    income_list = []

    for row in rows: 
        income_list.append(row)

    return render_template("income_overview.html", title="YMOYL - Income Overview", incomes = income_list)

@app.route("/expense_overview") # not working
def expense_overview():
    # details = request.form
    # expense_date = details['expense_date']
    # company = details['company']
    # catagory = details['catagory']
    # account = details ['account']
    # amount = details ['amount']
    # cur = mysql.connection.cursor()
    # mysql.connection.commit()
    cur = mysql.connection.cursor()
    cur.execute("select * from expense")
    rows =  cur.fetchall()
    cur.close()

    expense_list = []

    for row in rows: 
        expense_list.append(row)

    return render_template("expense_overview.html", title = "YMOYL - Expense Overview", expenses = expense_list)

@app.route("/investment_overview") # not working
def investment_overview():
    cur = mysql.connection.cursor()
    cur.execute("select * from investment")
    mysql.connection.commit()
    rows =  cur.fetchall()
    print(rows)
    cur.close()
    
    investment_list = []

    for row in rows: 
        investment_list.append(row)
    print(investment_list)
    return render_template("investment_overview.html", title = "YMOYL - Investment Overview", investment = investment_list)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
