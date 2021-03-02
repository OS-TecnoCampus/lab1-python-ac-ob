from fpdf import FPDF
import os

pdf = FPDF('P', 'mm', 'A4') #Creates the PDF
name = "Ex1" #HA D'AGAFAR EL NOM DEL FITXER

#First page (Title page)
pdf.add_page() #Adds a new page
pdf.set_margins(26.1, 23.3, 26.1) #Sets the margins
pdf.set_font('Arial', '', 30) #Sets the font and its style and size
pdf.set_line_width(4) #Sets the width of the line
pdf.set_draw_color(248, 172, 4) #Sets the color of the line (light orange)
pdf.line(26.1, 23.3, 26.1, 240) #Sets the position of the line

pdf.image('/home/devasc/labs/devnet-src/python/lab1-python-ac-ob/tecnocampus-logo.jpg', x=200, y=23.3, w=20) #Adds an image (logo)
pdf.set_xy(55, 70) #Sets in which x and y of the page starts writting
title = "Informació infraestructura de Xarxa TecnoCampus ("
text = title + name + ")"
pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L') #Writes the title
pdf.ln()
date = "Febrer 2021"
pdf.cell(w=0, h=0, txt=date, border=0, ln=2, align='L')

name = name + ".pdf"
filename = "/home/devasc/labs/devnet-src/python/lab1-python-ac-ob/" + name
pdf.output(filename, 'F') #Creates the pdf file