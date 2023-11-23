from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
matplotlib.use("agg")
app = Flask(__name__)

answer_page = "answer"

# Various helper functions:
def equation_definer(h:float, k:float, a:float):
    """An symbolic equation defined"""
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
    plt.title("General Graph")
    plt.grid(True)
    plt.savefig("./static/images/plot.jpg")
    plt.clf()
    return part1 + part2 + part3

def convert(number:str):
    """Converts a string to a float."""
    return float(request.form[number])
    
def vertex_solver(h, k, x, y):
    return (y-k)/(x-h)**2

def generalSolverCleaner(a, b, c):
    lists = [a, b, c]
    for index, i in enumerate(lists):
        if i == int(i):
            lists[index] = int(i)
    a, b, c = lists
    part0 = "y = "
    part1 = f"{a}x^2"
    part2 = f" + {b}x"
    part3 = f" + {c}"
    if a == 1:
        part1 = "x^2"

    if b == 0:
        part2 = ""
    elif b < 0:
        part2 = f" - {str(b)[1:]}x"
    
    if c == 0:
        part3 = ""
    elif c < 0:
        part3 = f" - {str(c)[1:]}"

    return part0 + part1 + part2 + part3
    


def generalSolver(x1, y1, x2, y2, x3, y3):
    regressioned = False
    inputs = [x1, x2, x3]
    outputs = [y1, y2, y3]
    x = np.array(inputs)
    y = np.array(outputs)
    X = np.vstack([np.ones(x.shape), x, x**2]).T
    try:
        coefficients = np.linalg.solve(X, y)
    except np.linalg.LinAlgError:
        try:
            coefficients = np.linalg.solve(X.T @ X, X.T @ y)
            regressioned = True
        except np.linalg.LinAlgError:
            return "Equation doesn't exist.", False
    if not (X @ coefficients == y).all() and regressioned:
        return "Equation doesn't exist.", False
    if coefficients[-1] == 0:
        return "The equation will yield a line, due to leading coefficient being zero.", False
    
    equation = generalSolverCleaner(coefficients[-1], coefficients[-2], coefficients[-3])
    # equation = f" y = {coefficients[-1]}x^2 + {coefficients[-2]}x + {coefficients[-3]}."

    xs = np.arange(np.min(x) - 2, np.max(x) + 2, step=1e-2)
    ys =  coefficients[-1] * xs**2 + coefficients[-2] * xs + coefficients[-3]
    plt.title("General Graph")
    plt.plot(xs, ys)
    plt.scatter(x, y, c='g')
    plt.legend("green")
    plt.grid(True)
    plt.savefig("./static/images/plot.jpg")
    plt.clf()
    return equation, True

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
def solve1():
    h = convert('vertexx')
    k = convert('vertexy')
    x = convert('pointx')
    y = convert('pointy')
    a = vertex_solver(h, k, x, y)
    equation = equation_definer(h, k, a)
    return render_template("answer1.html", equation=equation, plot_show=True)

@app.route('/answer2', methods=["POST"])
def solve2():
    x1, y1 = convert("x1"), convert("y1")
    x2, y2 = convert("x2"), convert("y2")
    x3, y3 = convert("x3"), convert("y3")
    equation, bools = generalSolver(x1, y1, x2, y2, x3, y3)
    return render_template("answer1.html", equation=equation, plot_show=bools)

# Error Handlers:
@app.errorhandler(404)
def handle404(error):
    return render_template("404.html"), 404

if __name__=="__main__":
    app.run(debug=True)