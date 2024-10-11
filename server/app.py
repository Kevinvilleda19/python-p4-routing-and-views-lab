#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Print the string in the console
    return param

# Route to display numbers up to the given integer
@app.route('/count/<int:param>')
def count(param):
    numbers = "\n".join(str(i) for i in range(0, param))
    return numbers + '\n'

# Route to handle math operations
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Error: Invalid operation"

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


