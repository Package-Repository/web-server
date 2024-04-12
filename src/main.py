from routes import entry, home, status
from app import flaskApp

if __name__ == '__main__':
	flaskApp.run(
		host='0.0.0.0',
		port=5000,
		debug=True,
		use_reloader=False # Otherwise would run scripts twice, leading to two bot instances
	)