import sqlite3
from flask import g

def init_db(app):
    def get_db():
        if 'db' not in g:
            g.db = sqlite3.connect(app.config['DATABASE'])
            g.db.row_factory = sqlite3.Row  # Optional: Makes row access easier (like dictionaries)
        return g.db

    @app.teardown_appcontext
    def close_connection(exception):
        db = g.pop('db', None)
        if db is not None:
            db.close()

    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS queries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                case_type TEXT,
                case_number TEXT,
                filing_year TEXT,
                response_html TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.commit()
    