import img2pdf
import sys
from PIL import Image
import os

#convert jpg to pdf! 
#usage python img2pdf.py xxx.jpg 
def conv_image(file_name, **kwargs):
    tmp = str(file_name).replace(".jpg", ".pdf")
    with open(tmp, "wb") as file:
        file.write(img2pdf.convert([file_name]))
        file.close()
    print("PDF created")
	
if __name__ == "__main__":
    conv_image(sys.argv[1])
