from flask import Flask, render_template
import os

app = Flask(__name__)
HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', '5000'))
DEBUG = bool(os.getenv('DEBUG', True))

@app.route('/')
def home_page():
    stage = os.getenv("STAGE", "Builder")
    return render_template("index.html", build_stage=stage)

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_404.html"), 404

if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
