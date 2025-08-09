def fetch_case_details(case_type, case_number, filing_year):
    # Replace this with actual scraping logic or Selenium later
    mock_data = {
        'parties': 'Spoorthi vs State',
        'filing_date': '01-01-2022',
        'next_hearing': '10-08-2025',
        'latest_order_link': 'https://example.com/sample_order.pdf'
    }

    # Return as structured HTML and raw HTML
    html_output = f"""
    <h2>Case Summary</h2>
    <p><strong>Parties:</strong> {mock_data['parties']}</p>
    <p><strong>Filing Date:</strong> {mock_data['filing_date']}</p>
    <p><strong>Next Hearing:</strong> {mock_data['next_hearing']}</p>
    <p><strong>Order:</strong> <a href="{mock_data['latest_order_link']}" target="_blank">View Order</a></p>
    """

    return html_output, html_output

