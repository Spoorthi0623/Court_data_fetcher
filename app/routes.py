from flask import Blueprint, render_template, request, current_app
from app.scraper import fetch_case_details
import sqlite3

routes = Blueprint('routes', __name__)  # changed from main → routes

@routes.route('/', methods=['GET', 'POST'])  # changed main → routes
def index():
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        filing_year = request.form['filing_year']

        try:
            result_data, raw_html = fetch_case_details(case_type, case_number, filing_year)

            db = sqlite3.connect(current_app.config['DATABASE'])
            db.execute("INSERT INTO queries (case_type, case_number, filing_year, response_html) VALUES (?, ?, ?, ?)",
                       (case_type, case_number, filing_year, raw_html))
            db.commit()
            db.close()

            return render_template('result.html', data=result_data)
        except Exception as e:
            return render_template('index.html', error=str(e))

    return render_template('index.html')
@routes.route('/history')
def history():
    db = sqlite3.connect(current_app.config['DATABASE'])
    cursor = db.execute("SELECT case_type, case_number, filing_year, timestamp FROM queries ORDER BY timestamp DESC")
    records = cursor.fetchall()
    db.close()
    return render_template('history.html', records=records)