from fpdf import FPDF
import datetime
import locale
import os

pdf = FPDF('P', 'mm', 'A4') #Creates the PDF
name = input("Enter the file name: ") #Asks the user to enter the name of the file
title = "Informació infraestructura de Xarxa TecnoCampus "

#First page (Title page)
def title_page():
    pdf.set_margins(26.1, 23.3, 26.1) #Sets the margins
    pdf.set_font('Arial', '', 30) #Sets the font and its style and size
    pdf.set_line_width(5) #Sets the width of the line
    pdf.set_draw_color(248, 172, 4) #Sets the color of the line (light orange)
    pdf.line(26.1, 23.3, 26.1, 245) #Sets the position of the line

    pdf.image('/home/devasc/labs/devnet-src/python/lab1-python-ac-ob/tecnocampus-logo.jpg', x=130, y=23.3, w=70) #Adds an image (logo)
    pdf.set_xy(40, 70) #Sets in which x and y of the page starts writting
    titlept1 = "Informació infraestructura"
    titlept2 = "de Xarxa TecnoCampus"
    pdf.cell(w=0, h=0, txt=titlept1, border=0, ln=2, align='L') #Writes the 1st lane of the title
    pdf.ln(12)
    pdf.set_x(40)
    pdf.cell(w=0, h=0, txt=titlept2, border=0, ln=2, align='L') #Writes the 2nd lane of the title
    pdf.ln(12)
    pdf.set_x(40)
    pdf.cell(w=0, h=0, txt="(" + name + ")", border=0, ln=2, align='L') #Writes the name of the Ex
    pdf.ln(30)
    pdf.set_x(40)

    locale.setlocale(locale.LC_ALL, 'ca_ES.UTF-8') #Sets locale to ca_ES to have the date in catalan
    dt = datetime.date.today()
    date = dt.strftime("%B %Y")
    pdf.cell(w=0, h=0, txt=date.replace("de ", "").capitalize(), border=0, ln=2, align='L') #Writes the date

#Header
def header():
    pdf.image('/home/devasc/labs/devnet-src/python/lab1-python-ac-ob/tecnocampus-logo-light.jpg', x=140, y=5, w=40) #Adds an image (logo)
    pdf.set_xy(26.1, 10)
    pdf.set_font('Arial', '', 11) #Sets the font and its style and size
    pdf.set_text_color(110, 110, 110) #Sets the color of the text (grey)
    pdf.cell(w=0, h=0, txt=title + "(" + name + ")", border=0, ln=0, align='L') #Writes the title
    
#Footer
def footer():
    pdf.set_xy(26.1, 276)
    pdf.set_font('Arial', '', 11) #Sets the font and its style and size
    pdf.set_text_color(110, 110, 110) #Sets the color of the text (grey)
    page = str(pdf.page_no()) #Gets the page number
    pdf.cell(w=0, h=0, txt=page, border=0, ln=0, align='L') #Adds a page number

pdf.add_page() #Adds a new page
title_page()
pdf.add_page() #Adds a new page
header()
footer()

name = name + ".pdf"
filename = "/home/devasc/labs/devnet-src/python/lab1-python-ac-ob/" + name
pdf.output(filename, 'F') #Creates the pdf file
