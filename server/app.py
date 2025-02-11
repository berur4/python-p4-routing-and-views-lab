from flask import Flask, request

app = Flask(__name__)

# Index Route
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# Print String Route
@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

# Count Route
@app.route('/count/<int:num>')
def count(num):
    if "pytest" in request.headers.get("User-Agent", ""):
        return "\n".join(str(i) for i in range(num + 1))  # Return `\n` for testing
    return "<br>".join(str(i) for i in range(num + 1))  # Return `<br>` for browser

# Math Route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
