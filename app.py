import os

from flask import (Flask, jsonify, redirect, render_template, request)

app = Flask(__name__)

users = {}


@app.route('/')
def login():
   print('Request for login page received')
   return render_template('login.html')

@app.route('/register')
def register():
   print('Request for register page received')
   return render_template('register.html')



@app.route('/dashboard')
def dashboard():
   print('Request for dashboard page received')
   return render_template('dashboard.html')

@app.route('/login', methods=['POST'])
def login_user():
   if request.is_json:
      data = request.get_json()

      username = data.get('username')
      password = data.get('password')

      if username in users:
        user = users[username]

        if password == user['password']:
           print('Login successful for user %s' % username)
           return jsonify({"message": "login successful"}), 200
        
        return jsonify({"error": "Login failed! Password did not match."}), 400

      # If the username does not exist, return a 404 error
      return jsonify({"error": "User not found"}), 404

@app.route('/user', methods=['POST'])
def create_user():
   if request.is_json:
      data = request.get_json()

      username = data.get('username')
      email = data.get('email')
      password = data.get('password')

    #   if username in users:
    #      return jsonify({"error": "Username already exists"}), 400
   
      users[username] = {'email': email, 'password': password}

      print('Request for create user received with username=%s email=%s password=%s' % (username, email, password))
      return jsonify({"message": "User created successfully"}), 201
   else:
        return jsonify({"error": "Invalid JSON data"}), 400


@app.route('/user/<username>')
def read_user(username):
    print('username is %s', users)
    if username in users:
        user = users[username]
        email = user['email']
        password = user['password']

        print('Request for read user received with username=%s email=%s password=%s' % (username, email, password))

        # Return user information as a JSON response
        return jsonify({"username": username, "email": email, "password": password})

    # If the username does not exist, return a 404 error
    return jsonify({"error": "User not found"}), 404


@app.route('/user/<username>', methods=['DELETE'])
def delete_user(username):
    if username in users:
        # Remove the user from the 'users' dictionary
        del users[username]

        print('Request for delete user received with username=%s' % username)

        # Return a success message as a JSON response
        return jsonify({"message": "User deleted successfully"})

    # If the username does not exist, return a 404 error
    return jsonify({"error": "User not found"}), 404



if __name__ == '__main__':
   app.run()
