from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)


@app.route('/')
def index():
    users = User.get_all_users()
    print(users)
    return render_template('index.html', users=users)


@app.route('/user/new', methods=["GET"])
def new_user():
    return render_template('create.html')

@app.route('/user/create', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.create_user(data)
    print(data)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)