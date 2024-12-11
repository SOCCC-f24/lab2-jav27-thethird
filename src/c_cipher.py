"""Jud-Arsenio Verrier, CSC138, 12/10/24"""

import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    Encrypts an input email string by shifting each letter up by 3 in ASCII.

    Args:
        email (str): Input string of length 6, with 3 letters followed by 3 digits.

    Returns:
        str: The encrypted string, or an error message if validation fails. 
    """
# Updated docstring for the encrypt function.
    output = "" 
    len_flag = len(email) != 6
    A = email[:3].isalpha()  # Check if the first 3 characters are letters
    B = email[3:].isdigit()  # Check if the last 3 characters are digits
    anum_flag = not (A and B)  # Flag if either condition is false
#TODO objective followed

    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     
        
    email_lst = list(email)
#TODO objective followed, processed string into list
        
    # TODO circumvented: Block shifts each character in the list
    for i in range(len(email_lst)):
        if email_lst[i].isalpha():  # Shift letters up by 3
            email_lst[i] = chr(ord(email_lst[i]) + 3)
        
    # TODO objective followed, convert list into a string
    email_str = ''.join(email_lst)

    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email_str
    return retVal 

def decrypt(email="def345"):
    """
    Decrypts an input email string by shifting each letter down by 3 in ASCII. 

    Args:
        email (str): Input string of length 6, with 3 letters followed by 3 digits.

    Returns:
        str: The decrypted string, or an error message if validation fails.   
    """
    # input validation
    output = "" 
    len_flag = len(email) != 6
# TODO objective followed, method repeated from earlier
    # keep all updates in the anum_flag (bool) variable
    A = email[:3].isalpha()  # Check first half (letters)
    B = email[3:].isdigit()  # Check second half (digits)
    anum_flag = not (A and B) 

    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   

    # TODO objective followed
    email_lst = list(email)  # Process the string into a list

    # Shift each character in the list
    for i in range(len(email_lst)):
        if email_lst[i].isalpha():  # Shift letters down by 3
            email_lst[i] = chr(ord(email_lst[i]) - 3)

    email_str = ''.join(email_lst)  # Convert list into a strin
    
    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = "aef345"
    return retVal
