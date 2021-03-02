def createPDF(self, name=None, size=None):
    from fpdf import FPDF
    import os
    pdf = new FPDF('P', 'cm', 'A4') #Creates the PDF
    name = #HA D'AGAFAR EL NOM DEL FITXER
    
    #First page (Title page)
    pdf.add_page() #Adds a new page
    pdf.set_margins(2.61, 2.33, 2.61) #Sets the margins
    pdf.set_font('Arial', '', 30) #Sets the font and its style and size
    pdf.set_xy(5.5, 7) #Sets in which x and y of the page starts writting
    title = "Informació infraestructura de Xarxa TecnoCampus ("
    text = title + name + ")"
    pdf.cell(0, 0, txt=text, 0, 2, align='L') #Writes the title
    
    pdf.outuput(name, 'F') #Creates the pdf file