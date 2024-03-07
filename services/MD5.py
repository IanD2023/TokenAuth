import hashlib
from random import choice
import string

def converter(string):
    
    MD5 = hashlib.md5(string.encode()).hexdigest()
    
    return MD5

def gerarhash():

    caracteres = string.ascii_uppercase + string.digits
    senha_segura = ''

    for i in range(6):
    
        senha_segura += choice(caracteres)

    return  senha_segura 

def gerarhashCodBarras():

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha_segura = ''

    for i in range(10):
    
        senha_segura += choice(caracteres)

    return  senha_segura    