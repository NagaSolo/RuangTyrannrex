from flask import Flask, request, render_template
app = Flask(__name__)

from modules.lapindromes import palindrome
from modules.fortytwo import fortytwo
from modules.flow007 import reversal

@app.route('/')
def home():
    return {}

@app.route('/lapindromes', methods=['GET', 'POST'])
def lapindromes():
    if request.method == 'POST':
        the_string = request.form["the_input"]
        return render_template('lapindromes.html', answer=f'The answer is {palindrome(the_string)}')
        # return {'Answer': palindrome(the_string)}
    else:
        # return f'Value is unspecified'
        return render_template('lapindromes.html')

@app.route('/fortytwo', methods=['GET', 'POST'])
def fortytworoute():
    if request.method == 'POST':
        the_string = request.form["the_answer"]
        return render_template('fortytwo.html', answer=f'The answer is {fortytwo(the_string)}')
    return render_template('fortytwo.html')

@app.route('/flow007', methods=['GET', 'POST'])
def flow_007():
    if request.method == 'POST':
        the_string = request.form["the_number"]
        return render_template('flow007.html', answer=f'Reversed form is {reversal(the_string)}')
    return render_template('flow007.html')

if __name__ == "__main__":
    app.run(debug=True)