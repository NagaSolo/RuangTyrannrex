from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api', methods=['GET'])
def home():
    return "Tyrannrex API"

if __name__ == "__main__":
    app.run()