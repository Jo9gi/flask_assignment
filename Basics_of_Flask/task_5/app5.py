'''5. Implement user sessions in a Flask app to store and display user-specific data.'''

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'my-secret-key' 

user_data = {
    'alice': 'Alice Johnson',
    'bob': 'Bob Smith',
    'charlie': 'Charlie Brown'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        if username in user_data:
            session['username'] = username  
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid username')
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']

        user_info = user_data.get(username, 'No data available')
        return render_template('dashboard.html', username=username, user_info=user_info)
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('username', None)  
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
