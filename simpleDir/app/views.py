from flask import render_template
from app import app
import socket


@app.route('/')
def time():
	hostname = socket.gethostname()
	ipaddress = socket.gethostbyname(socket.gethostname())
	return render_template('time.html', hostname=hostname, ipaddress=ipaddress)