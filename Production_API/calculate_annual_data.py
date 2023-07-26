import pandas as pd

# Load the data from the Excel file
data = pd.read_excel('data.xls')

# Group the data by API WELL NUMBER and sum the quarterly values to get the annual totals
annual_data = data.groupby('API WELL  NUMBER').sum()

# Define a function to retrieve the annual production for a given API WELL NUMBER
def get_annual_production(api_well_number):
    if api_well_number in annual_data.index:
        return {
            'oil': annual_data.loc[api_well_number, 'OIL'],
            'gas': annual_data.loc[api_well_number, 'GAS'],
            'brine': annual_data.loc[api_well_number, 'BRINE']
        }
    else:
        return None
