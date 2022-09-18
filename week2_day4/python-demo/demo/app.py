"""
    Entry point for my application
"""
import requests
from datetime import datetime
# import logging   #liberia para logins en python por default

URL = 'https://demo-api.free.beeceptor.com//my/api/path'

def get_demo_api_data():
    """
    GET data from Rest API Endpoint
    """
    #pass
    
    response = requests.get(URL)
    
    #en my app un status code de 200 significa error (DEPENDE DEL CONTEXTO DEL SISTEMA)
    #decido terminar o retornar empty data si ocurre esta condicion
    
    if response.status.code != 200:
        # add a logger
        # en lugar de hacer un print
        print(f'Request returned non OK value {response.status_code}')
        return [] #retorna empty data
        #raise Exception(f'Demo API returned {response.status_code}')  #termina
   
    # el endpoint devuelve un txt, othwerwise deberia usar el json() method
    return response.text


def write_data_in_file(data, filename, target_path=""):
    """
    Writes `data into` `filename`.
    `filename` lives in `target_path`
    """
    pass
    # TODO: Make sure non-empty target path exists 

    file = f"{target_path}{filename}" #funciona si target_path es vacío! 
    #TODO: Asegurar que funciona para non-empty path
    with open(file, 'w') as openfile:
        openfile.write(data)

#extract this function to utils.py(utils module)
def get_timestamp_string():
    return datetime.now().strftime("%Y%m&d%H%M%S")

def get_filename(prefix="log", extension="txt"):
    """
    Builds filename using `prefix` string,
    `suffix` string is build from timestamp yyyymmddHHMMSS
    and `extension` string
    output is: prefix_suffix.extension
    """
    # pass
    timestamp_string = get_timestamp_string()
    return "{}_{}.{}".format(prefix, timestamp_string, extension) #guion bajo entre valores y punto para la extension


def main ():
    #raise NotImplementedError
    #pass
    
    raw_data = get_demo_api_data()
    filename = get_filename()
    write_data_in_file(raw_data, filename, 'path/to')
    
main()
