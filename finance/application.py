import os
import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    #user enters by clicking a link
    if request.method=="GET":
        #retrieve purchase data for user
        row=db.execute("select key, sum(shares), s_name from purchase where user_id=? group by key", session["user_id"])
        p_t=0
        for i in row:
            #generating required data
            sp=lookup(i["key"])["price"]
            t=sp*i["sum(shares)"]
            i["c_p"]=sp
            i["total"]=t
            p_t=p_t+t
        #current cash for user
        a_t=db.execute("SELECT cash from users where id=?", session["user_id"])
        #current toal in portfolio
        t_t=a_t[0]["cash"]+p_t

        #generating index
        return render_template("index.html", row=row, grandtotal=t_t, cash=a_t[0]["cash"])

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():

    #User entered by clicking a link
    if request.method=="GET":
        return render_template("change_password.html")

    #user entered by submitting a form
    if request.method=="POST":
        currentpass=request.form.get("c_password")
        newpassword=request.form.get("password")
        confirmpass=request.form.get("confirm")

        #checking current password
        pa=db.execute("select hash from users where id=?", session["user_id"])
        if not check_password_hash(pa[0]["hash"], currentpass):
            return apology("Current password provided is wrong")

        #updating current password
        npass=generate_password_hash(newpassword)
        npa=db.execute("update users set hash=? where id=?", npass, session["user_id"])

        return redirect("/")



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    #user enters by clicking a link
    if request.method=="GET":
        return render_template("buy.html")

    #user enters by submitting a form
    if request.method=="POST":
        symbol=request.form.get("symbol")
        shares=request.form.get("shares")

        #checking inputs
        if not symbol or lookup(symbol)==None:
            return apology("Have to provide valid symbol.")
        if not shares:
            return apology("Have to provide shares")
        if shares.isnumeric()==False:
            return apology("Invalid shares")
        elif int(shares)<1:
            return apology("invalid shares")

        #generating data
        cash=db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])
        cost=lookup(symbol)["price"]*int(shares)

        if cost>cash[0]["cash"]:
            return apology("Not enough cash")

        #insert record of purchase into table
        db.execute("INSERT INTO purchase(user_id, key, s_name, shares, cost) VALUES(?,?,?,?,?)", session["user_id"], symbol, lookup(symbol)["name"], int(shares), cost)

        #updating current cash after transaction
        ca=cash[0]["cash"]-cost
        db.execute("UPDATE users SET cash=? WHERE id=?", ca, session["user_id"])

        #inserting record to maintain history
        db.execute("insert into history(user_id, transacted, shares, price, symbol) values(?,?,?,?,?)", session["user_id"], datetime.datetime.now(), int(shares), lookup(symbol)["price"], symbol)

        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    history=db.execute("select * from history where user_id=?", session["user_id"])
    return render_template("history.html", history=history)




@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    #user enterd via clicking a link
    if request.method=="GET":
        return render_template("quote.html")

    #user eneters via submitting a form
    if request.method=="POST":
        key=request.form.get("symbol")

        #checking inputs
        if not key:
            return apology("Key has to be provided")
        dic=lookup(key)
        if dic==None:
            return apology("No such stock found")

        return render_template("quoted.html",dic=dic)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    #user enters via a link
    if request.method=="GET":
        return render_template("register.html")

    #users enters via submitting a form
    if request.method=="POST":

        name=request.form.get("username")
        password=request.form.get("password")
        confirmation=request.form.get("confirmation")

        '''Checking inputs'''
        if not name:
            return apology("Name has to be provided.")
        us=db.execute("SELECT * FROM users")
        print (us)
        for i in us:
            if i["username"]==name:
                return apology("Name already exists.")
        if not password:
            return apology("Password has to be provided.")
        if confirmation!=password:
            return apology("Password and Confirmation have to be same.")

        #generating password hash to be stored in a the table
        ha=generate_password_hash(password)

        #inserting new user data into users table
        db.execute("INSERT INTO users(username,hash) VALUES(?,?)", name,ha)

        return redirect("/")





@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    #user enters via clicking a link
    if request.method=="GET":
        keys=db.execute("select distinct key from purchase where user_id=?", session["user_id"])
        return render_template("sell.html", keys=keys)

    #user enters via submitting a form
    if request.method=="POST":
        key=request.form.get("symbol")
        amt=request.form.get("shares")

        #checking inputs
        if amt.isnumeric()==False:
            return apology("Invalid shares")
        amt=int(amt)

        if not key:
            return apology("Symbol has to be provided")
        if not amt:
            return apology("Amount of shares has to be provided")
        if amt<0:
            return apology("Invalid number of shares")
        ns=db.execute("select sum(shares) from purchase where user_id=?", session["user_id"])
        if ns[0]["sum(shares)"]<amt:
            return apology("Not enough shares")

        #generating cash into user portfolio after transaction
        m=lookup(key)["price"]*amt
        cash=db.execute("select cash from users where id=?", session["user_id"])[0]["cash"]+m
        db.execute("update users set cash=? where id=?", cash, session["user_id"])

        #updating records
        shares=db.execute("select shares from purchase where user_id=? and key=?", session["user_id"], key)[0]["shares"]-amt
        db.execute("update purchase set shares=? where user_id=? and key=? limit 1", shares, session["user_id"], key)

        #updating user history
        db.execute("insert into history(user_id, transacted, shares, price, symbol) values(?,?,?,?,?)", session["user_id"], datetime.datetime.now(), -amt, lookup(key)["price"], key)

        return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
