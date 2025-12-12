from app import app

@app.route('/')
@app.route('/index')
def index():
	return 'home'

@app.route('/track')
def track():
	return 'track and calculate'

@app.route('/solutions')
def solutions():
	return 'solutions'

@app.route('/resources')
def resources():
	return 'resources'

@app.route('/account')
def account():
	return 'account'

