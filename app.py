from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
strap = Bootstrap(app)


# The real pages:
@app.route('/')
@app.route('/home')
def start():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

# Error Handlers:
@app.errorhandler(404)
def handle404(error):
    return render_template("404.html"), 404

if __name__=="__main__":
    app.run(debug=True)