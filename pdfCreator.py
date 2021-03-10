from fpdf import FPDF
import datetime
import locale
import yaml
import os

pdf = FPDF('P', 'mm', 'A4') #Creates the PDF
name = input("Enter the file name: ") #Asks the user to enter the name of the file
title = "Informació infraestructura de Xarxa TecnoCampus "
filename = '/home/devasc/labs/devnet-src/python/lab1-python-ac-ob/' + name
label = [] #Array to save the names of the devices

#obrir yaml i llegir el que li dius a for x in node: print(x["id"])
#with open(filename) as file:
    #ex = yaml.load(file, Loader=yaml.FullLoader)
    #node = ex["nodes"]
    #for x in node:
        #print(x["id"])

#Count number of nodes and links
with open(filename) as file:
    f = yaml.load(file, Loader=yaml.FullLoader)
    nodes = f["nodes"]
    for x in nodes:
        x["id"]
        label.append(x["label"]) #Saves the names of the devices
    links = f["links"]
    for x in links:
        x["id"]

print(len(nodes))
print(len(label))
for x in label:
    print(x)

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

#Tittle Page
pdf.add_page() #Adds a new page
title_page()
#Index
pdf.add_page() #Adds a new page
header()
footer()
#Introduction
pdf.add_page() #Adds a new page
header()
footer()
pdf.set_margins(26.1, 23.3, 26.1) #Sets the margins
pdf.set_xy(26.1, 23.3)
pdf.set_font('Arial', '', 16) #Sets the font and its style and size
pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
text = "1.- Introducció"
pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
pdf.ln(10)
pdf.set_font('Arial', '', 13) #Sets the font and its style and size
text = "1.1.- Descripció"
pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
pdf.ln(5)
pdf.set_font('Arial', '', 11) #Sets the font and its style and size
pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
text = "El present document descriu la topologia realitzada amb la configuració " + name + " a la empresa TecnoCampus."
pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
pdf.ln(5)
pdf.set_font('Arial', '', 13) #Sets the font and its style and size
pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
text = "1.2.- Objectius"
pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
pdf.ln(5)
pdf.set_font('Arial', '', 11) #Sets the font and its style and size
pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
text = "El objectiu d’aquest document és la de formalitzar el traspàs d’informació al equip tècnic responsable del manteniment de les infraestructures instal·lades. Aquesta informació fa referencia al disseny, instal·lació i configuració dels dispositius i sistemes afectats per la implementació.\nLa present documentació inclou:\n   - Descripció general de les infraestructures instal·lades.\n   - Configuració de les interfícies de xarxa.\n   - Configuració de les polítiques per les connexions VPN.\n   - Configuració dels protocols d’enrutament.\n   - Configuració de les llistes de control d’accés.\n   - Configuració dels banners."
pdf.multi_cell(w=0, h=5, txt=text.replace(u"\u2019", "'"), border=0, align='J', fill=False)
pdf.ln(5)
pdf.set_font('Arial', '', 13) #Sets the font and its style and size
pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
text = "1.3.- Descripció General de les infraestructures"
pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
pdf.ln(5)
pdf.set_font('Arial', '', 11) #Sets the font and its style and size
pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
text = "Actualment la topologia té la següent distribució:"
pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
pdf.ln(5)
text = "En aquesta topologia tenim " + str(len(nodes)) + " equips, connectats a través de " + str(len(links)) + " links."
pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
pdf.ln(7)
#Devices Configuration
pdf.set_font('Arial', '', 16) #Sets the font and its style and size
pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
text = "2.- Configuració dels dispositius"
pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
pdf.ln(5)
pdf.set_font('Arial', '', 11) #Sets the font and its style and size
pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
text = "A continuació, es detalla la configuració dels diferents dispositius:"
pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
pdf.ln(5)
pdf.set_font('Arial', '', 13) #Sets the font and its style and size
pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
text = "2.1.- " + label[0]
pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
pdf.ln(7)
text = "2.1.1- Interfícies"
pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
pdf.ln(5)
pdf.set_font('Arial', '', 11) #Sets the font and its style and size
pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
text = "Les interfícies i la seva configuració és:"
pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
pdf.ln(5)

pdf.add_page() #Adds a new page
header()
footer()

name = name + ".pdf"
filename = "/home/devasc/labs/devnet-src/python/lab1-python-ac-ob/" + name
pdf.output(filename, 'F') #Creates the pdf file
