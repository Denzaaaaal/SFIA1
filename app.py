from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="YMOYL")
    return render_template("login.html", title="YMOYL")
    

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
