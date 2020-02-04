#File to identify errors into the response on the whois command

def find_whois_error(text=''):
    """
    Method used to find possible errors from the whois command. These error are related to domains without a whois record.
    """
    whois_errors = ["no match", "no entries found" , "No whois server is known" , "nameserver not found" , "not found", "No match", "No entries found"]        
    error = ''

    if text != '':

        for w in whois_errors:
            if text.find(w) != -1:
                error = 'Whois not found'
                return error
                    
    return error 