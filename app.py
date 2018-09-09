from bottle import route, run, error, template, redirect, abort, get, response
from sys import argv

@get('/')
def redir():
    redirect('/home')
@get('/<name>')
def index(name):
    if name == 'home':
        return '<h1>Home</h1>' \
               '<a href="/home">Home</a><br><a href="/about">About</a><br><a href="/contact">Contact</a>'
    elif name == 'about':
        return '<h1>About</h1>' \
               '<a href="/home">Home</a><br><a href="/about">About</a><br><a href="/contact">Contact</a>'
    elif name == 'contact':
        return '<h1>Contact</h1>' \
               '<a href="/home">Home</a><br><a href="/about">About</a><br><a href="/contact">Contact</a>'
    else:
        abort(404)
@error(404)
def error404(error):
    return '<h1>villa</h1>'
bottle.run(host='0.0.0.0', port=argv[1])
