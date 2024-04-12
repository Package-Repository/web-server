from flask import redirect
from app import flaskApp

@flaskApp.route("/")
def entry():
	return redirect("/home")