from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Define the API endpoint to retrieve the annual data
@app.route('/data')
def get_annual_data():
    # Get the API WELL NUMBER from the request parameters
    api_well_number = request.args.get('well')

    # Connect to the SQLite database
    conn = sqlite3.connect('annual_data.db')
    cursor = conn.cursor()

    # Query the database for the annual production data
    cursor.execute('''
        SELECT oil, gas, brine
        FROM annual_production
        WHERE api_well_number = ?
    ''', (api_well_number,))

    # Fetch the result
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    # Return the result as JSON
    if result:
        return jsonify({
            'oil': result[0],
            'gas': result[1],
            'brine': result[2]
        })
    else:
        return jsonify({'error': 'Data not found'})

if __name__ == '__main__':
    app.run(port=8080)
