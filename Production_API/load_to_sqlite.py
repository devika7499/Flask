import pandas as pd
import sqlite3

# Load the data from the Excel file
data = pd.read_excel('data.xls')

# Group the data by API WELL NUMBER and sum the quarterly values to get the annual totals
annual_data = data.groupby('API WELL  NUMBER').sum()

# Connect to the SQLite database
conn = sqlite3.connect('annual_data.db')
cursor = conn.cursor()

# Create a table to store the annual data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS annual_production (
        api_well_number TEXT PRIMARY KEY,
        oil INTEGER,
        gas INTEGER,
        brine INTEGER
    )
''')

# Insert the annual data into the database
for api_well_number, row in annual_data.iterrows():
    cursor.execute('''
        INSERT INTO annual_production (api_well_number, oil, gas, brine)
        VALUES (?, ?, ?, ?)
    ''', (api_well_number, row['OIL'], row['GAS'], row['BRINE']))

# Commit the changes and close the connection
conn.commit()
conn.close()
