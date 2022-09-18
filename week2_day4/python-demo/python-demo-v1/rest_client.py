import requests
#import loggin (buscar e implementar loggin python)

URL = 'https://demo-api.free.beeceptor.com//my/api/path'

def get_demo_api_data():
    """
    GET data from Rest API Endpoint
    """
    
    response = requests.get(URL)
    
   
    if response.status_code != 200:
        #TODO: add a logger (tener informacion historica de la ejecucion)
        print(f'Request returned non OK value {response.status_code}')
        return
        
    return response.text

