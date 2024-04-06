##lambda_function
import logging

import contact_us
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# initializing size of string 
def lambda_handler(event, context):
    logger.info('Received message: %s', event)
    http_method = event.get('httpMethod')
    
        
    path = (event.get('path').split("/")[1]) 
   
    if http_method == 'OPTION':
        response = {
            statusCode: 200,
            headers: {
                        'Content-Type' : 'application/json',
                        'Access-Control-Allow-Origin' : '*',
                        'Allow' : 'GET, OPTIONS, POST,DELETE',
                        'Access-Control-Allow-Methods' : 'GET, OPTIONS, POST,DELETE',
                        'Access-Control-Allow-Headers' : '*'
                }
                }
    else:
        if path == "contactform":
            response = contact_us.lambda_handler(event, context)
    
    logger.info("Response: %s", response)
    return response