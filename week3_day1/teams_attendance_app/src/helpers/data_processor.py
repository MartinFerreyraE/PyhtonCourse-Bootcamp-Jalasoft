"""
    Filters in-memory meetings data and uses meeting_name, star_date, end_date, etc...
"""
from datetime import datetime
from helpers import json_processor, csv_processor

def transform_string_into_date(string_date, format_date='%Y/%m/%d'):
    return datetime.strptime(string_date, format_date)

def enter_dates():

    start_input = input('Enter a start date in YYYY/MM/DD format: ')
    end_input = input('Enter a end date in YYYY/MM/DD format: ')

    try:
        transform_string_into_date(start_input, format_date='%Y/%m/%d')
        transform_string_into_date(end_input, format_date='%Y/%m/%d')
    except Exception:
        print('\Please use the correct format')
        return enter_dates()

    return start_input, end_input
