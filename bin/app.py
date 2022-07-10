from bottle import route, run, static_file

@route('/<filepath:path>')
def index(filepath):
	return static_file(filepath, root='./templates')

run(host='0.0.0.0', port=8000,debug=True)
