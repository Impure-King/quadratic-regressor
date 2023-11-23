from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
matplotlib.use("agg")
app = Flask(__name__)

answer_page = "answer"

# An Error handling class:
class IncorrectInput(object):
    """Initialized with the error message and prevents faulty inputs. 
    Arguments:
        - Error (str): A string consisting of all the error message."""
    def __init__(self, error: str) -> None:
        self.error_message = error

# Various helper functions:
def equation_definer(h:float, k:float, a:float):
    lists = [h, k, a]
    for index, i in enumerate(lists):
        if i == int(i):
            lists[index] = int(i)
    h, k, a = lists
    part1 = "y = "
    part2 = "(x - h)^2"
    part3 = " + k"
    if h == 0:
        part2 = "x^2"
    elif h < 0:
        part2 = f"(x + {(h**2)**0.5})^2"
    else:
        part2 = f"(x - {h})^2"
    
    if a == 0:
        part2 = ""
    elif a != 1:
        part2 = str(a) + part2
    
    if k == 0:
        part3 = ""
    elif k < 0:
        part3 = f" - {(k**2)**0.5}"
    else:
        part3 = f" + {k}"


    # Handling the graphing:
    x = np.arange(-100, 100)
    y = a * (x - h)**2 + k
    plt.plot(x, y)
    plt.savefig("./static/images/plot.jpg")
    plt.clf()
    return part1 + part2 + part3

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
    return render_template("project1.html", answer_page=answer_page, plot_show=False)

# Solved page:
@app.route('/' + answer_page, methods=["POST"])
def solve1():
    h = convert('vertexx')
    k = convert('vertexy')
    x = convert('pointx')
    y = convert('pointy')
    a = vertex_solver(h, k, x, y)
    equation = equation_definer(h, k, a)
    return render_template("project1.html", equation=equation, plot_show=True)

@app.route('/answer2', methods=["POST"])
def solve2():
    x1, y1 = convert("x1"), convert("y1")
    x2, y2 = convert("x2"), convert("y2")
    x3, y3 = convert("x3"), convert("y3")
    return render_template("project1.html", equation=1)

# Error Handlers:
@app.errorhandler(404)
def handle404(error):
    return render_template("404.html"), 404

if __name__=="__main__":
    app.run(debug=True)