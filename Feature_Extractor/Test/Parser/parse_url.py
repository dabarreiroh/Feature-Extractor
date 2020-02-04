import re
from query import command_query
from exceptions import InvalidURL
from errors import find_whois_error

#Class to extract the domain or subdomins that compound the url

class Parser_url():
    """
    Class to identify the domain name from an url and to remove its http/https protocol and path.
    This class has two private attibures where the domain and url information is going to be store: domain and url.
    The only information requiered is the url, it does not matter how the url is entered. 
    """

#Class attributes

    __url = ""
    __domain = ""

    #Init Function
    def __init__(self,url):

        if url == '' or url == None:
            #function to validate a url()
            print('the url is empty or not valid')
        else:
            self.set_url(url)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    #Setters and getters from the domain and url variables
    def set_url(self,url):
        """
        Parser_url method to store the url entered to the private url attribute
        """
        if type(url) is str:
            self.__url = url.lower().strip()
        else:
            InvalidURL()

    def get_url(self):
        """
        Parser_url method to return the private url attribute
        """
        return self.__url

    def set_domain(self,domain):
        """
        Parser_url method to store the domain into the private domain attribute
        """
        self.__domain = domain
       
    def get_domain(self):
        """
        Parser_url method to return the private domain attribute
        """
        return self.__domain

#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------

    # Funcion para remover el https o http de una url en caso de la misma exista.
    # Funcion to remove the word https o http from the url in case it exists
    def remove_http(self):
        """
        Method to remove the protocol http/https/ftp from the url entered if existed
        """

        if re.search("https",self.get_url()):
            self.set_url(self.get_url().replace('https://',''))
        elif re.search("http",self.get_url()):
            self.set_url(self.get_url().replace('http://',''))
        elif re.search("ftp",self.get_url()):
            self.set_url(self.get_url().replace('ftp://',''))
        else:
            pass

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # Funcion para eliminar los folder de una url, en el caso de que los mismos existaa, el proceso debe ser implementado junto con la funcion remove_http()
    # Function to remove the url's folders, in case they do exists, the process must be implemented along side with remove_http() function.   
    def remove_folders(self):
        """
        Method to remove paths from the url entered https://example.com/paths..../../..
        """

        l = self.get_url().split('/')
        l.reverse()
        self.set_url(''.join(l[-1])) 
        l = self.get_url().split(':')
        l.reverse()
        self.set_url(re.sub('/','',self.get_url()))

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    #The url should be previously parse to use this function
    #The function analise only three subdomain to set the domain name
    #The function uses the whois command response to validate the domain name
    #The function does not return nothing it modifies the domain attribute
    def find_domain(self):
        """
        Method to extract the domain name from a url, it uses the reposnse from the whois command to identify the domain name  
        """
        #self.set_url(url)
        self.remove_http()
        self.remove_folders()

        dom = self.get_url().split('.')

        #El cuerpo de la url ya corresponde en si mismo a un dominio.
        if self.get_url().count('.') == 1:
           self.set_domain(self.get_url()) 
        #Caso Www
        elif dom[0].count("w") >= 3 and len(dom[0]) <= 5:
            self.set_domain(".".join(dom[1:])) 
        
        #Use the whois function to validate and discover the domain, in case there were several subdomains into the url       
        elif self.get_url().count('.') > 1: #El espacio del dominio tiene mas de dos subdominios
            #Seleccionar los campos de los ultimos cuatro espacios en el caso de que existan
            point = self.get_url().count('.')
            l = self.get_url().split('.')
            l4 = l[0:4]   #"La funcion solo toma hasta cuatro campos para realizar el analisis"
            pdom = '.'.join(l4)
            #case something.something.domain.tld
            if point >= 3:
                    #command_query(command = "whois " + pdom,TimeOut=4)
                if l4[0].count("w") >= 3 and len(l4[0]) <= 5: #"si contiene www"
                    self.set_domain(".".join(l4[1:]))
                    #print('flag1') 
                elif find_whois_error(command_query(command = "whois " + pdom,TimeOut=4)) != 'Whois not found':
                    self.set_domain(pdom)
                    #print('flag2')
                elif l4[1].count("w") >= 3 and len(l4[1]) <= 5: #"si contiene www"
                    self.set_domain(".".join(l4[2:]))
                    #print('flag3')
                elif find_whois_error(command_query(command= "whois " + '.'.join(l4[1:]),TimeOut=4 )) != 'Whois not found': #three fields
                    self.set_domain('.'.join(l4[1:]))
                    #print('flag4')
                else:
                    self.set_domain('.'.join(l4[2:]))
                    #print('flag5')

            # case something.domain.tld
            elif point == 2:
                
                if l4[1].count("w") >= 3 and len(l4[1]) <= 5: #"si contiene www"
                    self.set_domain(".".join(l4[2:]))
                    #print('flag6')
                elif find_whois_error(command_query(command = "whois " + '.'.join(l4[1:]),TimeOut=4)) != 'Whois not found': #three fields
                    self.set_domain('.'.join(l4[1:]))
                    #print('flag7')
                else:
                    self.set_domain('.'.join(l4[2:]))
                    #print('flag8')

            else:
                self.set_domain('.'.join(l4[2:]))
                #print('flag9')

        else:
            print("No domain")
        #    InvalidURL()
            

#url = Parser_url("http://json.parser.online.fr/")
#url.find_domain()
#print(url.get_domain())















