from flask import Flask, jsonify, url_for, abort, request
from passlib.apps import custom_app_context as pwd_context
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    basedir, 'db.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


@app.route('/api/v3.0/users', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(404)
    if User.query.filter_by(username=username).first() is not None:
        abort(404)
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'username': user.username
    }), 201, {
        'Location': url_for('get_user', id=user.id, _external=True)
    }


@app.route('/api/v3.0/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(404)
    return jsonify({'username': user.username})


if __name__ == '__main__':
    app.run(debug=True)
