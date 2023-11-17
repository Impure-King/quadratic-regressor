from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

answer_page = "9"

# An Error handling class:
class IncorrectInput(object):
    """Initialized with the error message and prevents faulty inputs. 
    Arguments:
        - Error (str): A string consisting of all the error message."""
    def __init__(self, error: str) -> None:
        self.error_message = error


# Parsing the coordinates:
def convert(number:str):
    try:
        return float(request.form([number]))
    except:
        return IncorrectInput(f"""A numerical value is not inputted.
                                  A numerical value is an rational number written with in arabic numerals.
                                  Additionally ensure that an extra '-' or an extra '+' is not inputted.
                                  Don't be an idiot.
                                  Current Value {number}.""")

def vertex_solver(h, k, x, y):
    if x == h:
        return IncorrectInput("When using ver")

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
    h = convert('vertexx')
    k = convert('vertexy')
    x = convert('pointx')
    y = convert('pointy')
    try:
        a = (y - k)/(x - h)**2
    except:
        a = 1
    return render_template("answer1.html", equation=f"y = {a}(x - {h})^2 + {k}", valid_input=True)

# Error Handlers:
@app.errorhandler(404)
def handle404(error):
    return render_template("404.html"), 404

if __name__=="__main__":
    app.run(debug=True)