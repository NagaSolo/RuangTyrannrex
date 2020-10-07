from flask import Flask, request, render_template
app = Flask(__name__)

from modules.lapindromes import palindrome
from modules.fortytwo import fortytwo
from modules.flow007 import reversal
from modules.zco14003 import max_profit_from_budget

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fortytworoute')
def route_life():
    return render_template('fortytwo.html')

@app.route('/flow_007')
def route_flow007():
    return render_template('flow007.html')

@app.route('/lapindromes')
def route_lapindromes():
    return render_template('lapindromes.html')

@app.route('/route_zco14003')
def route_zco14003():
    return render_template('zco14003.html')

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

@app.route('/zco14003', methods=['GET', 'POST'])
def opt_prices():
    if request.method == 'POST':
        the_string = request.form["the_budget"]
        return render_template('zco14003.html', answer=f'Reversed form is {max_profit_from_budget(the_string)}')
    return render_template('zco14003.html')

if __name__ == "__main__":
    app.run(debug=True)