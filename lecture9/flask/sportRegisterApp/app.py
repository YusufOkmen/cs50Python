from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = ["Basketball", "Soccer", "Swimming"]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")
    else:
        return render_template("success.html")
    

if __name__ == "__main__":
    app.run(debug=True) 