'''6. Build a Flask app that allows users to upload files and display them on the website.'''

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Folder to store uploaded files
app.secret_key = 'my-secret-key'  # Set a secret key for session management

# Create the uploads folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        # Save the uploaded file
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return redirect(url_for('display_file', filename=file.filename))
    return render_template('upload.html')

@app.route('/display/<filename>')
def display_file(filename):
    return render_template('display.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
