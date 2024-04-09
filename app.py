# app.py
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

mysql_pwd = os.environ.get('MYSQL_PASSWORD')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:"+mysql_pwd+"@localhost/user_data"
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'username': user.username, 'email': user.email} for user in users]
    return jsonify(user_list)

@app.route('/swagger')
def swagger():
    return render_template('swagger.html')

if __name__ == '__main__':
    app.run(debug=True)
