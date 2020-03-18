from flask import Flask, render_template, request, redirect, url_for
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

@app.route("/income_overview", methods = ['GET','POST']) # Completed
def income_overview():
    cur = mysql.connection.cursor()
    cur.execute("select * from income")
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
            cur.execute("insert into income (id, date_of_income, company, amount) values (%s, %s, %s, %s);", (ID, Date_Of_Income, Company, int(Amount)))
        if request.form['action'] == 'delete':
            cur.execute("delete from income where id = %s and date_of_income = %s and amount = %s;", (ID, Date_Of_Income, int(Amount)))
        if request.form ['action'] == 'update':
            cur.execute("update income set date_of_income = %s, company = %s, amount = %s where id = %s;", (Date_Of_Income, Company, int(Amount), ID)) 
        mysql.connection.commit() 
        return redirect(url_for('income_overview'))
    return render_template("income_overview.html", title="YMOYL - Income Overview", incomes = income_list)

@app.route("/expense_overview", methods = ['GET','POST']) # Completed
def expense_overview():
    cur = mysql.connection.cursor()
    cur.execute("select * from expense")
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
        cur = mysql.connection.cursor()
        if request.form['action'] == 'submit':
            cur.execute("insert into expense (id, expense_date, company, description, catagory, account, amount) values (%s, %s, %s, %s, %s, %s, %s);", (ID, Expense_Date, Company, Description, Catagory, Account, int(Amount)))
        if request.form['action'] == 'delete':
            cur.execute("DELETE FROM expense WHERE id = %s and expense_date = %s and description = %s;", (ID, Expense_Date, Description))
        if request.form['action'] == 'update':
            cur.execute("update expense set expense_date = %s, company = %s, description = %s, catagory = %s, account = %s, amount = %s where id = %s;", (Expense_Date, Company, Description, Catagory, Account, int(Amount), ID))
        mysql.connection.commit()   
        cur.close()
        return redirect(url_for('expense_overview'))     
    return render_template("expense_overview.html", title = "YMOYL - Expense Overview", expenses = expense_list)

@app.route("/investment_overview", methods = ['GET','POST']) # Completed
def investment_overview():
    cur = mysql.connection.cursor()
    cur.execute("select * from investment")
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
        Regular_Investment = details['regular_investment']
        Dividend_Investment = details['dividend_investment']
        Dividend_Amount = details['dividend_amount']
        cur = mysql.connection.cursor()
        if request.form['action'] == 'submit':
            cur.execute("insert into investment (id, ticker, description, quantity, price, value, cost, regular_investment, dividend_reinvestment, dividend_amount) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (ID, Ticker, Description, Quantity, Price, Value, Cost, Regular_Investment, Dividend_Investment, Dividend_Amount))
        if request.form['action'] == 'delete':
            cur.execute("delete from investment where id = %s and ticker = %s and description = %s;", (ID, Ticker, Description))
        if request.form['action'] == 'update':
            cur.execute("update investment set ticker = %s, description = %s, quantity = %s, price = %s, value = %s, cost = %s, regular_investment = %s, dividend_reinvestment = %s, dividend_amount = %s where id = %s;", (Ticker, Description, Quantity, Price, Value, Cost, Regular_Investment, Dividend_Investment, Dividend_Amount, ID))
        mysql.connection.commit()
        return redirect(url_for('investment_overview'))
    return render_template("investment_overview.html", title = "YMOYL - Investment Overview", investment = investment_list)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
