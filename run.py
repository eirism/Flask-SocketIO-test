from iris import app, socketio
socketio.run(app, port=app.config['PORT'])
