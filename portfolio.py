from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')

def main():
    return render_template("index.html")

@app.route('/portfolio')

def portfolio():
    return render_template("portfolio.html")
@app.route('/about')

def about():
    return render_template("about.html")

app.run(debug=True)
