from glob import glob
import os 

import fpdf
from pdf_maker import Pdf_maker

def lambda_maker():
    
    
    # try:    
        
        maker = Pdf_maker()
        maker.pdfmaker()
        return True
    # except Exception as ex:
        return f"Problem with {ex}"
    
    
            


