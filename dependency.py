# Important Computing libraries:
import numpy as np
from numpy import ndarray
import plotly.graph_objects as po
import plotly.express as px



# Creating various reusable functions for equation defining:

def vertex_equation_concatenator(h:float, k:float, a:float) -> str:
    """The equation creates string representing the equation of a parabola in vertex points,
    when given the leading coefficient, x-vertex, and the y-vertex point. It symbolically 
    optimizes the string to remove parts based on mathematical conventions.
    
    Arguments:
        h (float): A decimal indicating the x-vertex value of the parabola.
        k (float): A decimal indicating the y-vertex value of the parabola.
        a (float): A decimal indicating the leading coefficient of the parabola. Also known as the vertical stretch factor."""
    # Keeping a list for looping:
    lists: list = [h, k, a]

    # Looping through and checking if any argument is an int:
    for index, i in enumerate(lists):
        if i == int(i):
            lists[index] = int(i)
    
    # Changing the values:
    h, k, a = lists

    # Starting string concatenation:
    part1: str = "y = "
    part2: str = f"(x - {h})^2"
    part3: str = f" + {k}"

    # Checking various special cases.
    if h == 0:
        part2 = "x^2"
    elif h < 0:
        part2 = f"(x + {abs(h)})^2"
    
    if a == 0:
        part2 = ""
    elif a != 1:
        part2 = str(a) + part2
    
    if k == 0:
        part3 = ""
    elif k < 0:
        part3 = f" - {abs(k)}"
    
    # Handling final graphing:
    x: ndarray = np.arange(int(-1e2), int(1e2 + 1)) 

    # Getting the y values:
    y: ndarray = a * (x - h)**2 + k

    # Graphing the results:
    fig = px.line(x = x, y = y, title="General Graph", labels={"x":"x-axis", "y":"y-axis"})
    fig.write_html("./templates/image.html")

    equation = part1 + part2 + part3

    return equation


def general_equation_concatenator(a:float, b: float, c: float) -> str:
    """The alternative of the ``equation_definer``, where all the coefficients of the general equation is known.
    Returns the string of a simplified equation.
    
    Arguments:
        a (float): A decimal denoting the leading coefficient of the quadratic.
        b (float): A decimal denoting the secondary coefficient of the quadratic.
        c (float): A decimal denoting the constant of the quadratic.
    """
    # Creating a list that can be parsed:
    lists: list = [a, b, c]
    for index, i in enumerate(lists):
        if i == int(i):
            lists[index] = int(i) # Continuing to list
    
    a, b, c = lists # Reassigning the values.
    
    # Piecewise Equation concatenator:
    part0: str = "y = "
    part1: str = f"{a}x^2"
    part2: str = f" + {b}x"
    part3: str = f" + {c}"
    if a == 1:
        part1 = "x^2"
    elif a == 0:
        part1 = ""

    if b == 0:
        part2 = ""
    elif b < 0:
        part2 = f" - {str(b)[1:]}x"
    
    if c == 0:
        part3 = ""
    elif c < 0:
        part3 = f" - {str(c)[1:]}"

    return part0 + part1 + part2 + part3

# Helper Functions for solving the equation:

def leading_coefficient_solver(h:float, k:float, x:float, y:float) -> float:
    """A basic solver for the vertical stretch factor of a parabola, when given the vertex coordinates and another point.

    Arguments:
        h (float): The x-vertex of the parabola.
        k (float): The y-vertex of the parabola.
        x (float): The abscissa of the additional point.
        y (float): The ordinate of the additional point.
    """
    return (y - k)/(x - h)**2

def coefficient_solver(x1, x2, x3, y1, y2, y3):
    """A symbolic coefficient solver. The derivation will be provided below.
    
    Arguments:
        x1 (float): A decimal number.
        x2 (float): A decimal number.
        x3 (float): A decimal number.
        y1 (float): A decimal number.
        y2 (float): A decimal number.
        y3 (float): A decimal number.
    
    Derivation:
    ```markdown

    $ax_1^2 + bx_1 + c = y_1$

    $ax_2^2 + bx_2 + c = y_2$

    $ax_3^2 + bx_3 + c = y_3$

    $\implies$ The following:

    $f(x) = a(x_1^2 - x_3^2) + b(x_1 - x_3) = y_1 - y_3$

    $g(x) = a(x_2^2 - x_3^2) + b(x_2 - x_3) = y_2 - y_3$

    which can be:

    $(x_2 - x_3)f(x) - (x_1 - x_3)g(x) = (y_1 - y_3)(x_2 - x_3) - (y_2 - y_3)(x_1 - x_3)$

    $\implies[(x_1^2 - x_3^2)(x_2 - x_3) - (x_2^2 - x_3^2)(x_1 - x_3)]a = (y_1 - y_3)(x_2 - x_3) - (y_2 - y_3)(x_1 - x_3)$

    $a = \frac{(y_1 - y_3)(x_2 - x_3) - (y_2 - y_3)(x_1 - x_3)}{(x_1 - x_2)(x_2 - x_3)(x_1 - x_3)}$
    ```
    """

    # Calculating the a-coordinate:
    a = ((y1-y3)*(x2-x3) - (y2-y3)*(x1-x3))/((x1-x2)*(x2-x3)*(x1-x3))
    
    # Calculating the b coordinate:
    b1 = ((y1 - y3) - (x1**2 - x3**2) * a)/(x1 - x3)
    b2 = ((y2 - y3) - (x2**2 - x3**2) * a)/(x2 - x3)
    if not b1 == b2:
        return False
    b = b1

    # Calculating the c coordinate:
    c1 = y1 - a*x1**2  - b*x1
    c2 = y2 - a*x2**2  - b*x2
    c3 = y3 - a*x3**2  - b*x3
    if not (c1 == c2 and c1 == c3 and c2 == c3):
        return False
    c = c1
    return [c, b, a]

# Complete solver:
def complete_general_equation_solver(x1, y1, x2, y2, x3, y3):
    """A complete solver that can plot solve and do anything."""
    inputs = [x1, x2, x3]
    outputs = [y1, y2, y3]
    x = np.array(inputs)
    y = np.array(outputs)
    X = np.vstack([np.ones(x.shape), x, x**2]).T
    coefficients = coefficient_solver(x1, x2, x3, y1, y2, y3)
    coefficients = np.linalg.solve(X, y)

    if isinstance(coefficients, bool):
        try:
            coefficients = np.linalg.solve(X, y)
        except:
            return "The Equation doesn't exist.", False

    equation = general_equation_concatenator(coefficients[-1], coefficients[-2], coefficients[-3])

    # Graphing the values:
    xs = np.arange(np.min(x) - 2, np.max(x) + 2, step=1e-2)
    ys =  coefficients[-1] * xs**2 + coefficients[-2] * xs + coefficients[-3]
    fig = px.line(x=xs, y=ys, title="General Graph", labels={"x": "x-axis", "y": "y-axis"})
    fig.write_html("./templates/image.html")

    if coefficients[-1] == 0:
        return "The equation will yield a line, due to leading coefficient being zero.\n" + equation, True

    return equation, True