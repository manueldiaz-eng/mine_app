from flask import Flask, render_template
from info import info

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html', info=info)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)