from flask import Flask

app = Flask(__name__)



@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = range (parameter)
    numbers_text = '\n'.join(map(str,numbers)) + '\n'
    return numbers_text

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1,operation,num2):
    try:
        #convert into an integer
        number1 = int(num1)
    except ValueError:
        #if its a float
        try:
            number1 = float(num1)
        except ValueError: 
            #if it is neither
            return "Invalid input for num1"
        
    try:
        #convert into an integer
        number2 = int(num2)
    except ValueError:
        #if its a float
        try:
            number2 = float(num2)
        except ValueError: 
            #if it is neither
            return "Invalid input for num1"
    
    result = None
    
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == 'div':
        if number2 != 0:
            result = number1 / number2
        else:
            return "You cannot divide by zero"
    elif operation == '%':
        result = number1 % number2
    else:
        return "Please enter a valid operation. i.e +, -, *, div, %"    
    
    return str(result)
    
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)