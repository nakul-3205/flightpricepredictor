import pandas as pd
from datetime import datetime

def prepare_simple_input(date_str, stops, airline, source, dest, feature_columns):
    date = datetime.strptime(date_str, "%d %B %Y")

    input_dict = dict.fromkeys(feature_columns, 0)
    input_dict.update({
        'Total_Stops': int(stops.split()[0]),
        'date': date.day,
        'month': date.month,
        'year': date.year,
    })

    for cat in [f'Airline_{airline}', f'Source_{source}', f'Destination_{dest}']:
        if cat in input_dict:
            input_dict[cat] = 1

    return pd.DataFrame([input_dict])
