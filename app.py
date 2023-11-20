from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

answer_page = "current_answer"

# An Error handling class:
class IncorrectInput(object):
    """Initialized with the error message and prevents faulty inputs. 
    Arguments:
        - Error (str): A string consisting of all the error message."""
    def __init__(self, error: str) -> None:
        self.error_message = error


def convert(number:str):
    """Converts a string to a float."""
    return float(request.form[number])
    
def vertex_solver(h, k, x, y):
    return (y-k)/(x-h)**2

# The real pages:
@app.route('/')
@app.route('/home')
def start():
    return render_template("home.html")

# Actual Project input page:
@app.route('/Quadratic Regressor')
def project():
    return render_template("project1.html", answer_page=answer_page)

# Solved page:
@app.route('/' + answer_page, methods=["POST"])
def solve():
    valid_input = True
    h = convert('vertexx')
    k = convert('vertexy')
    x = convert('pointx')
    y = convert('pointy')
    a = vertex_solver(h, k, x, y)
    if isinstance(a, IncorrectInput):
        valid_input=False
        equation=a.error_message
    else:
        equation = f"y = {a}(x - {h})^2 + {k}"
    return render_template("answer1.html", equation=equation, valid_input=valid_input)

# Error Handlers:
@app.errorhandler(404)
def handle404(error):
    return render_template("404.html"), 404

if __name__=="__main__":
    app.run(debug=True)