from barcode import Code128
from datetime import date
from services import MD5
import os

def geraCodigo(codigo,hash):
    
    if codigo != "":
        
      codBarras = Code128(codigo)

      arquivo=("tokenbag/static/img/codBarras/"+hash)
         
      codBarras.save(arquivo) 