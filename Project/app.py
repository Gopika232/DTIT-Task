from flask import Flask, send_from_directory    #type:ignore
from backend.routes import routes
from backend.database import create_table
from backend.profile import profile
from backend.reports import reports
from backend.notification import notification

app = Flask(__name__)

create_table()

app.register_blueprint(routes)
app.register_blueprint(profile)
app.register_blueprint(reports)
app.register_blueprint(notification)

@app.route("/")
def home():
    return send_from_directory("frontend","login.html")


@app.route("/login")
def login_page():
    return send_from_directory("frontend","login.html")

@app.route("/register")
def register_page():
    return send_from_directory("frontend","register.html")

@app.route("/dashboard")
def dashboard():
    return send_from_directory("frontend","dashboard.html")
@app.route("/profile")
def profile():
    return send_from_directory("frontend","profile.html")


@app.route("/reports")
def reports():
    return send_from_directory("frontend","reports.html")


@app.route("/admin")
def admin():
    return send_from_directory("frontend","admin.html")
@app.route("/<path:file>")
def files(file):
    return send_from_directory("frontend",file)

if __name__=="__main__":
    app.run(debug=True)