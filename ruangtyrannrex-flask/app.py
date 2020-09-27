from flask import Flask, request
app = Flask(__name__)

from modules.lapindromes import palindrome

@app.route('/')
def home():
    return f'Ruang Tyrannrex'

@app.route('/lapindromes', methods=['GET', 'POST'])
def lapindromes():
    if request.method == 'POST':
        the_string = request.values.get()
        return {'Answer': palindrome(the_string)}
    else:
        return f'Value is unspecified'