import mysql.connector
from flask import Flask,request,jsonify

app = Flask(__name__)

db = mysql.connector.connect(
    port = "3307",
    host = "localhost",
    user = "root",
    password = "",
    database = "flaskdb"
)

cursor = db.cursor()
@app.route("/users",methods=["GET"])
def get_users():
    cursor.execute("SELECT * FROM users")
    return jsonify(cursor.fetchall())

if __name__ == "__main__":
    app.run(debug=True)
