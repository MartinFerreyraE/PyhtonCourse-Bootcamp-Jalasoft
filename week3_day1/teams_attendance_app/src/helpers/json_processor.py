import json
from datetime import datetime

def write_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def generate_filename(filename="arguments", extension="json"):
    dt = datetime.now()
    date_time_sufix = dt.strftime("%m%d%Y%H%M%S")
    return "{}_{}.{}".format(filename, date_time_sufix, extension)

