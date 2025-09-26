from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3307/flaskdb'
db = SQLAlchemy(app)
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

@app.route("/users", methods=["GET"])
def get_users():
    users = Users.query.all()
    return jsonify([{'id': u.id, 'name': u.name, 'email': u.email} for u in users])

if __name__ == "__main__":
    app.run(debug=True)