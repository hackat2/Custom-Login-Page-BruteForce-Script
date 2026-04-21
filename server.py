from flask import Flask, request

app = Flask(__name__)

# Create the login page route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Grab what the attacker script typed into the form
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Check if the credentials match our hardcoded secret
        if username == 'admin' and password == 'supersecret':
            return "<h1>Welcome Dashboard</h1><p>Login Successful!</p>"
        else:
            return "<h1>Access Denied</h1><p>Invalid Password</p>"
    
    # If it's a GET request, just show the HTML login form
    return '''
        <h2>Internal Portal Login</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    # Run the server on port 5000
    app.run(port=5000)
