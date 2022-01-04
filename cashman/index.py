from flask import Flask, jsonify, request
from .model.expense import Expense, ExpenseSchema
from .model.income import Income, IncomeSchema
from .model.transaction_type import TransactionType

app = Flask(__name__)


transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('pizza', 15),
    Expense('Rock Concert', 30)
]


@app.route('/')
def home():
    return 'hello'


@app.route('/incomes/')
def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = schema.dump(
        filter(lambda t: t.type == TransactionType.INCOME, transactions)
    )

    return jsonify(incomes)


# leaving out trailing slash to account for redirect of POST request
@app.route('/incomes', methods=['POST'])
def add_income():
    print('request.get_json():', dict(request.get_json()))

    income = IncomeSchema().load(request.get_json())

    print(income)

    transactions.append(income)

    return '', 204


@app.route('/expenses/')
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(
        filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
    )

    return jsonify(expenses)


@app.route('/expenses', methods=['POST'])
def add_expenses():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
