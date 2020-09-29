from flask import Flask, request, render_template
app = Flask(__name__)

from modules.lapindromes import palindrome

@app.route('/')
def home():
    return f'Ruang Tyrannrex'

@app.route('/lapindromes', methods=['GET', 'POST'])
def lapindromes():
    if request.method == 'POST':
        the_string = request.form["the_input"]
        return render_template('lapindromes.html', answer=f'The answer is {palindrome(the_string)}')
        # return {'Answer': palindrome(the_string)}
    else:
        # return f'Value is unspecified'
        return render_template('lapindromes.html')