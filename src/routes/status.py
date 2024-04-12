from flask import request, render_template
import dimscord_bobot as bot
from app import flaskApp

@flaskApp.route('/status', methods=['POST', 'GET'])
def status():
	if request.method == 'POST':
		bot.update_status(request.form['status'], request.form['message'])
		bot.wait()

	activity = bot.get_activity()
	activity = "" if activity == None else activity

	return render_template("bot_controls.html", status=bot.get_status(), message=activity)
