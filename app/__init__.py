from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '8mf4<1M4I,6|okZ=Qt)4'
    
    from .routes import main
    app.register_blueprint(main)
    
    return app