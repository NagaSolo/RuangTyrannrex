from flask import Flask
app = Flask(__name__)

from modules.lapindromes import palindrome

@app.route('/')
def home():
    return f'Ruang Tyrannrex'

@app.route('/lapindromes')
def lapindromes():
    the_string = 'kocok'
    return {'Answer': palindrome(the_string)}