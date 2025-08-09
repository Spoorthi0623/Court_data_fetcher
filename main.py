import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

from flask import Flask
from app.database import init_db
from app.routes import routes

# Create Flask app
app = Flask(__name__)
app.config['DATABASE'] = 'court_cases.db'

# Initialize database
init_db(app)

# Register the routes blueprint
app.register_blueprint(routes)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)