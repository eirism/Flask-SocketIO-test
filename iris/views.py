from flask import render_template
from flask_socketio import emit
from iris import app, models, db, socketio


@app.route('/')
@app.route('/index')
def index():
    all_texts = models.Text.query.all()
    return render_template('index.html', texts=all_texts)


@socketio.on('my_event')
def handle_text(message):
    new_text = models.Text(content=message)
    db.session.add(new_text)
    db.session.commit()
    emit('brd_text', message, broadcast=True)


@socketio.on('connect')
def client_connect():
    print('Client connected')
