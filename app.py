# Important imports
from flask import (Flask, render_template, request)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from dependency import (coefficient_solver,
                       vertex_equation_concatenator,
                       general_equation_concatenator,
                       leading_coefficient_solver,
                       complete_general_equation_solver)

matplotlib.use("agg")

# Starting the application:
app = Flask(__name__)

# Naming the redirect link:
answer_page = "/answer"

# defining step:
step_val = "0.001"

# Helper function:

def get_value(input_name:str):
    """Returns a float value when given the name of the input_box.
    Arguments:
        input_name (string): A string denoting the name of the input.
    """
    return float(request.form[input_name])    


# The real pages:
@app.route('/')
@app.route('/home')
def start():
    return render_template("home.html")

# Actual Project input page:
@app.route('/Quadratic Regressor')
def project():
    return render_template("project1.html", answer_page=answer_page, step = step_val)

# Solved page:
@app.route('/' + answer_page, methods=["POST"])
def solve1():
    h = get_value('vertexx')
    k = get_value('vertexy')
    x = get_value('pointx')
    y = get_value('pointy')
    a = leading_coefficient_solver(h, k, x, y)
    equation = vertex_equation_concatenator(h, k, a)
    with open("./equation.txt", "w") as file:
        file.write(equation)
    return render_template("answer1.html", equation=equation, plot_show=True)

@app.route('/answer2', methods=["POST"])
def solve2():
    x1, y1 = get_value("x1"), get_value("y1")
    x2, y2 = get_value("x2"), get_value("y2")
    x3, y3 = get_value("x3"), get_value("y3")
    equation, bools = complete_general_equation_solver(x1, y1, x2, y2, x3, y3)
    with open("./equation.txt", "w") as file:
        file.write(equation)
    return render_template("answer1.html", equation=equation, plot_show=bools)

# Optional Features:
@app.route('/desmos')
def desmos():
    with open('./equation.txt', "r") as file:
        value = file.read()
    return render_template("desmos.html", value=value)

@app.route('/image')
def image():
    return render_template("image.html")

# Error Handlers:
@app.errorhandler(404)
def handle404(error):
    return render_template("404.html"), 404

if __name__=="__main__":
    app.run(debug=True)