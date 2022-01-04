from flask import Flask, jsonify, request
app = Flask(__name__)


incomes = [
    { 'description': 'salary', 'amount': 5000 }
]


@app.route('/')
def home():
    return 'hello'


@app.route('/incomes/')
def get_incomes():
    return jsonify(incomes)

# leaving out trailing slash to account for redirect of POST request
@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())

    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
