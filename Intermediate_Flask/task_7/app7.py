# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['POST'])
def add_item():
    new_item_name = request.form.get('item_name')
    new_item = Item(name=new_item_name)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_item', methods=['POST'])
def delete_item():
    item_id = request.form.get('item_id')
    item_to_delete = Item.query.get(item_id)
    if item_to_delete:
        db.session.delete(item_to_delete)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/update_item/<int:item_id>', methods=['POST', 'GET'])
def update_item(item_id):
    updated_name = request.form.get('updated_name')
    item_to_update = Item.query.get(item_id)
    if item_to_update:
        item_to_update.name = updated_name
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8000)