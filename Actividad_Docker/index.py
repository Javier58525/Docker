from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('login.html')

@app.route("/loged",methods=["GET", "POST"])
def loged():
    return render_template('loged.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)