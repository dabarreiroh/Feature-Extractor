import re
import ssl
import errors
import socket
import parse_url
from query import command_query
from parse_response import jsonparser

#Procedure to extract all the whois information from the whois and dig linux command
#
# Find the domain name
# Find the registrar whois server
# Find IP address
# Find whois related to IP address
# Retrive a Json with information gathered

class Whois():

    def __init__(self):
        pass
        #self.whois(url) 
        #a = jsonparser(filename = 'whois.txt',dict = jsonparser(filename='whoisip.txt',keyword='Network Whois Record',dict = jsonparser(filename='IP.txt',keyword='Address lookup',dict = jsonparser(filename='ssl.txt',keyword='SSL Certificate'))),keyword='Domain Whois Record')
        #print(a)  

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def ssl(self,url):

        if url != '' or url != None:

            hostname = parse_url.Parser_url(url)
            hostname.remove_http()
            hostname.remove_folders()

            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(socket.socket(), server_hostname=hostname.get_url())
            s.connect((hostname.get_url(), 443))

            return s.getpeercert()
        else:
            return None

    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
       
    def whois(self,dom):
        
        #whois = parse_url.Parser_url(url)
        #whois.find_domain()
        #whois.set_url(url)
        #whois.find_domain()

        w = command_query(command='whois '+ str(dom))
        ip = command_query(command='dig '+ str(dom) + ' +short' )
        
        #print("whois: {} \n Ip: {}".format(w,ip))
        adress = ip.split('\n')

        for ipv4 in adress:

            points = len(re.findall(r"\.",ipv4))
            letters = len(re.findall(r"[a-zA-Z]",ipv4)) 
            #print(linea + " " + str(nip) + " " +str(points) )

            if len(re.findall(r"2[0-5][0-5]|1[0-9][0-9]|[0-9][0-9]|[0-9]|[a-zA-Z]",ipv4)) >= 4 and points == 3 and letters == 0:               
                wip = command_query(command='whois ' + ipv4,TimeOut=10)
                break
            else:
                wip = ''

        try:
            match = re.search( r"Registrar WHOIS Server:(.*)",w,re.I).group() #.group()  #.string.split(':')[-1].strip()
        except:
            match = ''
        else:
            wserver = match.split(':')[-1].strip()

        if match == '' or match == None:
            response = {'w':w,'w_server':'','ip':ip,'w_ip':wip}
        else:
            #print('whois '+ whois.get_domain() + ' -h ' + wserver)
            w_server = command_query(command='whois '+ dom + ' -h ' + wserver, TimeOut= 10) #change to whois.txt
            response = {'w':w,'w_server':w_server,'ip':ip,'w_ip':wip}
        #print("whois server: {}".format(w))

        return response

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
                 
            
            
        
#test = whois('http://json.parser.online.fr/')


#a = Whois()
#print(a.whois('facebook.com'))
#p = requests.get('https://yahoo.com/')
#print(p.headers)


#z = whois('')
#a = z.ssl('yahoo.com')
#print(a)












