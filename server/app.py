#!/usr/bin/env python3

from flask import Flask,Response

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>', methods=['GET'])
def print_text(parameter):
    # Print the text to the console
    print(parameter)
    # Return the text as a response
    return Response(parameter, mimetype='text/plain')

@app.route('/count/<int:parameter>', methods=['GET'])
def get_counts(parameter):
    def generate_numbers():
        for i in range(parameter):
            yield f"{i}\n"
    return Response(generate_numbers(), mimetype='text/plain')

@app.route('/math/<int:num1>/<operation>/<int:num2>', methods=['GET'])
def math_operation(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return Response("Invalid operation", status=400)
    
    return Response(str(result), mimetype='text/plain')


    
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
