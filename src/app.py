from flask import Flask, render_template as flask_render_template

flaskApp = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

flaskApp.config['SESSION_TYPE'] = 'filesystem'
flaskApp.config['SESSION_PERMANENT'] = True