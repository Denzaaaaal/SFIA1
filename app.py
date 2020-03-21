from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Referencing Configuration variables
app.config["MYSQL_HOST"] = os.environ.get('MYSQLHOST')
app.config["MYSQL_USER"] = os.environ.get('MYSQLUSER')
app.config["MYSQL_PASSWORD"] = os.environ.get('MYSQLPASSWORD')
app.config["MYSQL_DB"]  = os.environ.get('MYSQLDB')


mysql = MySQL(app)

app.config['SECRET_KEY'] = 'secret'

# Login page
@app.route("/", methods = ['GET', 'POST']) # Authenicate password
def login(): 
    # Login and redirect user to account_overview
    if request.method == "POST":
        details = request.form
        Username = details['username']
        Password = details['passwd']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user_details WHERE username = %s AND passwd = %s", (Username, Password))
        mysql.connection.commit()
        rows = cur.fetchall()
        cur.close()

        # Saving User details
        info = []

        for i in rows:
            for j in i:
                info.append(j)

        session['user_id'] = info[0]
        session['first_name'] = info[3]
        return redirect(url_for('account_overview'))

    return render_template("index.html", title = "YMOYL - Home Page")

# Creating a new user
@app.route("/sign_up", methods = ['GET','POST'])
def sign_up():
    # Create user and redirect to login page
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
        return redirect(url_for('login'))

        info = []

    for row in rows: 
        info.append(row)
    return render_template("sign_up.html", title = "YMOYL - Sign up", info1 = info)

# Reading total values from income, investment and expense table for a specific user
@app.route("/account_overview", methods = ['GET']) # Add up totals for user
def account_overview():
    cur = mysql.connection.cursor()
    userid = session['user_id']
    first_name = session['first_name']
    cur.execute("SELECT first_name FROM user_details WHERE id = %s;", [userid])
    mysql.connection.commit()
    cur.close()
    tincome = 100
    texpense = 200
    tinvestment = 300
    return render_template("account_overview.html", title = "YMOYL - Account Overview", name = first_name, tincome = tincome, texpense = texpense, tinvestment = tinvestment)

# CRUD functionality on income page
@app.route("/income_overview", methods = ['GET','POST'])
def income_overview():
    cur = mysql.connection.cursor()
    userid = session['user_id']
    cur.execute("SELECT * FROM income WHERE usr_id = %s", [userid])
    mysql.connection.commit()
    rows =  cur.fetchall()
    cur.close()

    income_list = []

    for row in rows: 
        income_list.append(row)

    if request.method == 'POST':
        details = request.form
        ID = details['id']
        
        Date_Of_Income = details['date_of_income']
        Company = details['company']
        Amount = details['amount']
        cur = mysql.connection.cursor()
        if request.form['action'] == 'submit':
            cur.execute("INSERT INTO income (date_of_income, company, amount, usr_id) VALUES (%s, %s, %s, %s);", (Date_Of_Income, Company, int(Amount), userid))
        if request.form['action'] == 'delete':
            cur.execute("DELETE FROM income WHERE id = %s AND date_of_income = %s AND amount = %s;", (ID, Date_Of_Income, int(Amount)))
        if request.form ['action'] == 'update':
            cur.execute("UPDATE income SET date_of_income = %s, company = %s, amount = %s where id = %s;", (Date_Of_Income, Company, int(Amount), ID)) 
        mysql.connection.commit() 
        return redirect(url_for('income_overview'))
    return render_template("income_overview.html", title="YMOYL - Income Overview", incomes = income_list)

# CRUD Functionality on expense page
@app.route("/expense_overview", methods = ['GET','POST'])
def expense_overview():
    cur = mysql.connection.cursor()
    userid = session['user_id']
    cur.execute("SELECT * FROM expense WHERE usr_id = %s;", [userid])
    rows =  cur.fetchall()
    cur.close()
    
    expense_list = []

    for row in rows: 
        expense_list.append(row)

    if request.method == 'POST':
        details = request.form
        ID = details['id']
        Expense_Date = details['expense_date']
        Company = details['company']
        Description = details['description']
        Catagory = details['catagory']
        Account = details['account']
        Amount = details['amount']
        User_id = session['user_id']
        cur = mysql.connection.cursor()
        if request.form['action'] == 'submit':
            cur.execute("INSERT INTO expense (expense_date, company, description, catagory, account, amount, usr_id) VALUES (%s, %s, %s, %s, %s, %s, %s);", (Expense_Date, Company, Description, Catagory, Account, int(Amount), User_id))
        if request.form['action'] == 'delete':
            cur.execute("DELETE FROM expense WHERE id = %s AND expense_date = %s AND description = %s;", (ID, Expense_Date, Description))
        if request.form['action'] == 'update':
            cur.execute("UPDATE expense SET expense_date = %s, company = %s, description = %s, catagory = %s, account = %s, amount = %s where id = %s;", (Expense_Date, Company, Description, Catagory, Account, int(Amount), ID))
        mysql.connection.commit()   
        cur.close()
        return redirect(url_for('expense_overview'))     
    return render_template("expense_overview.html", title = "YMOYL - Expense Overview", expenses = expense_list)

# CRUD functionality on Investment page
@app.route("/investment_overview", methods = ['GET','POST']) 
def investment_overview():
    cur = mysql.connection.cursor()
    user_id = session['user_id']
    cur.execute("SELECT * FROM investment WHERE usr_id = %s;", [user_id])
    rows =  cur.fetchall()
    cur.close()
    
    investment_list = []

    for row in rows: 
        investment_list.append(row)

    if request.method == 'POST':
        details = request.form
        ID = details['id']
        Ticker = details['ticker']
        Description = details['description']
        Quantity = details['quantity']
        Price = details['price']
        Value = details['value']
        Cost = details['cost']
        User_id = session['user_id']
        Regular_Investment = details['regular_investment']
        Dividend_Investment = details['dividend_investment']
        Dividend_Amount = details['dividend_amount']
        cur = mysql.connection.cursor()
        if request.form['action'] == 'submit':
            cur.execute("INSERT INTO investment (ticker, description, quantity, price, value, cost, regular_investment, dividend_reinvestment, dividend_amount, usr_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (Ticker, Description, Quantity, Price, Value, Cost, Regular_Investment, Dividend_Investment, Dividend_Amount, User_id))
        if request.form['action'] == 'delete':
            cur.execute("DELETE FROM investment WHERE id = %s AND ticker = %s AND description = %s;", (ID, Ticker, Description))
        if request.form['action'] == 'update':
            cur.execute("UPDATE investment SET ticker = %s, description = %s, quantity = %s, price = %s, value = %s, cost = %s, regular_investment = %s, dividend_reinvestment = %s, dividend_amount = %s WHERE id = %s;", (Ticker, Description, Quantity, Price, Value, Cost, Regular_Investment, Dividend_Investment, Dividend_Amount, ID))
        mysql.connection.commit()
        return redirect(url_for('investment_overview'))
    return render_template("investment_overview.html", title = "YMOYL - Investment Overview", investment = investment_list)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
