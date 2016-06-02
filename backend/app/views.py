import time
from flask import render_template
from app import app

@app.route('/')
@app.route('/time')
def return_time():
	return time.asctime()