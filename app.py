from flask import Flask, get_flashed_messages, request, jsonify, redirect, session, render_template, flash, url_for

app = Flask(__name__)

app.secret_key = 'disneyrulez'


users = {
    'user': 'password'
}

@app.route('/')
def startPage():
    return render_template('startPage.html')

@app.route('/loginPage')
def loginPage():
    return render_template('login.html')

@app.route('/signupPage')
def signupPage():
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login ():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return render_template('main.html')
        else:
            flash("Incorrect Username or Password")
            return render_template('login.html')
    else:
        return render_template('main.html')


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm = request.form['password']

        if username in users:
            return redirect(url_for('/signup'))
        if password != confirm:
            return redirect(url_for('/signup'))
        
        users[username] = password
        return redirect(url_for('/main'))
    return render_template('main.html')



@app.route('/generator')
def generator():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)


#Idea: Quote Generator
#Functions:
#Generates Quotes from a given 55-ish
#Takes in Quotes to add into the list of quotes


#Requirements:
#user-id so that each user can have their own quotes







#3 GET -> Request data from a specified resource
#1 POST -> Create a resource





#Unused Code For Future Reference:


#Gets username and password, but they show up in the url
# @app.route('/handle_get', methods=['GET'])
# def handle_get():
#     if request.method == 'GET':
#         username = request.args['username']
#         password = request.args['password']
#         print(username, password)
#         if username in users and users[username] == password:
#             return '<h1>Welcome!!!</h1>'
#         else:
#             return '<h1>invalid credentials!</h1>'
#     else:
#         return render_template('login.html')






#Beginer Guide

# @app.route("/")
# def home():
#     return "Hello"

# @app.route("/get-user/<user_id>")
# def get_user(user_id):
#     user_data = {
#         "user_id": user_id,
#         "name": "Joh Doe",
#         "email": "john.doe@example.com"
#     }

#     extra = request.args.get("extra")
#     if extra:
#         user_data["extra"] = extra

#     return jsonify(user_data), 200

# @app.route("/create-user", methods=["POST"])
# def create_user():
#     data = request.get_json()
#     return jsonify(data), 201
