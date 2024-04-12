from flask import request, redirect, render_template
from app import flaskApp
from stuff import actions

@flaskApp.route("/home", methods=['POST', 'GET'])
def home():
	if request.method != 'POST':
		return render_template('index.html')
	
	inp = request.form['button']

	action = actions.get(inp)
	if action is not None:
		action.execute()
		if action.redirect:
			return redirect(f"/{inp}")
	
	return render_template("index.html")
