from fpdf import FPDF
import datetime
import os

pdf = FPDF('P', 'mm', 'A4') #Creates the PDF
name = "Ex1" #HA D'AGAFAR EL NOM DEL FITXER

#First page (Title page)
pdf.add_page() #Adds a new page
pdf.set_margins(26.1, 23.3, 26.1) #Sets the margins
pdf.set_font('Arial', '', 30) #Sets the font and its style and size
pdf.set_line_width(4) #Sets the width of the line
pdf.set_draw_color(248, 172, 4) #Sets the color of the line (light orange)
pdf.line(26.1, 23.3, 26.1, 245) #Sets the position of the line

pdf.image('/home/devasc/labs/devnet-src/python/lab1-python-ac-ob/tecnocampus-logo.jpg', x=130, y=23.3, w=70) #Adds an image (logo)
pdf.set_xy(40, 70) #Sets in which x and y of the page starts writting
title1 = "Informació infraestructura"
title2 = "de Xarxa TecnoCampus"
ex = "(" + name + ")"
pdf.cell(w=0, h=0, txt=title1, border=0, ln=2, align='L') #Writes the 1st lane of the title
pdf.ln(15)
pdf.set_x(40)
pdf.cell(w=0, h=0, txt=title2, border=0, ln=2, align='L') #Writes the 2nd lane of the title
pdf.ln(15)
pdf.set_x(40)
pdf.cell(w=0, h=0, txt=ex, border=0, ln=2, align='L') #Writes the name of the Ex
pdf.ln(30)
pdf.set_x(40)

dt = datetime.datetime.today()
date = dt.strftime("%B %Y")
pdf.cell(w=0, h=0, txt=date, border=0, ln=2, align='L') #Writes the date

name = name + ".pdf"
filename = "/home/devasc/labs/devnet-src/python/lab1-python-ac-ob/" + name
pdf.output(filename, 'F') #Creates the pdf file