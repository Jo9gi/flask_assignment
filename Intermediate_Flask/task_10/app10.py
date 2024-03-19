'''10. Design a Flask app with proper error handling for 404 and 500 errors.'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "HELLO FRIENDS THIS IS OUR 404 AND 500 ERROR HANDELLER WEBSITE"
# Custom error handler for 404 Not Found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Custom error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

# Your routes and other app logic go here...

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8005)