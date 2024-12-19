from flask import Flask
from routes import book_routes, member_routes, search
from auth import auth_routes
import os
from dotenv import load_dotenv
from functools import wraps


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Register Blueprints
app.register_blueprint(book_routes, url_prefix='/books')
app.register_blueprint(member_routes, url_prefix='/members')
app.register_blueprint(auth_routes)
app.register_blueprint(search, url_prefix='/search')


if __name__ == '__main__':
    app.run(debug=True)
