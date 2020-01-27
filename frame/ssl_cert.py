
#Document to extract the url ssl and parse it response in dictionary format

import ssl, socket
import parse_url



#funtion to extrac the ssl

 #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def ssl_certificate(url):
    """
    The ssl_certficate extract the ssl certificate information from an url.
    This method requires that the url without paths!!  
    """

    if url != '' or url != None:
        
        hostname = url
        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
        s.connect((hostname, 443))
        #cert = s.getpeercert()

        return  parse_ssl_response(s.getpeercert())

    else:

        return {}



#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def parse_ssl_response(data={}):
    """
    This method gathers the information from ssl_certificated() method and returns it in a dictionary
    """
    
    dicc = {}

    for value in data.keys():
    
        if type(data[value]) == tuple:
            dicc[value] = [data[value][v] for v in range(len(data[value]))]
        else:
            dicc[value] = data[value]

    return dicc



#a = ssl_certificate('python.org')
#print(a)





