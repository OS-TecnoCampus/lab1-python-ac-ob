from fpdf import FPDF
import datetime
import locale
import yaml
import os
import networkx as nx 
import matplotlib.pyplot as plt

pdf = FPDF('P', 'mm', 'A4') #Creates the PDF
name = input("Enter the file name: ") #Asks the user to enter the name of the file
title = "Informació infraestructura de Xarxa TecnoCampus "
indexLinks = []
indexPages = []
label = [] #Array to save the names of the devices
conf = [] #Array to save the configuration of the devices

#To get the information inside yaml file
with open(name) as file:
    f = yaml.load(file, Loader=yaml.FullLoader)
    nodes = f["nodes"]
    for x in nodes:
        x["id"] #Counts number of nodes
        label.append(x["label"]) #Saves the names of the devices
        conf.append(x["configuration"])
    links = f["links"]
    for x in links:
        x["id"] #Counts number of links

#First page (Title page)
def title_page():
    pdf.set_margins(26.1, 23.3, 26.1) #Sets the margins
    pdf.set_font('Arial', '', 30) #Sets the font and its style and size
    pdf.set_line_width(5) #Sets the width of the line
    pdf.set_draw_color(248, 172, 4) #Sets the color of the line (light orange)
    pdf.line(26.1, 23.3, 26.1, 245) #Sets the position of the line
    pdf.image('tecnocampus-logo.jpg', x=130, y=23.3, w=70) #Adds an image (logo)
    pdf.set_xy(40, 70) #Sets in which x and y of the page starts writting
    titlept1 = "Informació infraestructura"
    titlept2 = "de Xarxa TecnoCampus"
    pdf.cell(w=0, h=12, txt=titlept1, border=0, ln=2, align='L') #Writes the 1st lane of the title
    pdf.set_x(40)
    pdf.cell(w=0, h=12, txt=titlept2, border=0, ln=2, align='L') #Writes the 2nd lane of the title
    pdf.ln(7)
    pdf.set_x(40)
    pdf.cell(w=0, h=0, txt="(" + name + ")", border=0, ln=2, align='L') #Writes the name of the Ex
    pdf.ln(30)
    pdf.set_x(40)
    locale.setlocale(locale.LC_ALL, 'ca_ES.UTF-8') #Sets locale to ca_ES to have the date in catalan
    dt = datetime.date.today()
    date = dt.strftime("%B %Y")
    pdf.cell(w=0, h=0, txt=date.replace("de ", "").capitalize(), border=0, ln=2, align='L') #Writes the date
    pdf.set_xy(26.1, 260)
    pdf.set_font('Arial', '', 8) #Sets the font and its style and size
    pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
    text = "La informació continguda en aquest document pot ser de caràcter privilegiat i/o confidencial. Qualsevol disseminació, distribució o copia d’aquest document per qualsevol altre persona diferent als receptors originals queda estrictament prohibida. Si ha rebut aquest document per error, sis plau notifiquí immediatament al emissor i esborri qualsevol copia d’aquest document."
    pdf.multi_cell(w=0, h=3, txt=text.replace(u"\u2019", "'"), border=0, align='J', fill=False) #Writes the bottom banner

#Header
def header():
    pdf.image('tecnocampus-logo-light.jpg', x=140, y=5, w=40) #Adds an image (logo)
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

#Function to get the interfaces
def getInterfaces(device, stringConf):
    interfaces = [] #Array to save the interfaces configuration
    id = [] #Array to save the links id from the interfaces
    lab = [] #Array to save the links label from the interfaces
    interfaces = (nodes[device]["interfaces"])
    for x in interfaces:
        string = str(x)
        posId = string.find("i") + 6
        id.append(string[posId:posId+2])
        posLabel = string.find("label") + 9
        endLabel = string.find("', 'type'")
        lab.append(string[posLabel:endLabel])
    for x in range(len(id)):
        i = x
        text = "   -  Link " + id[i] + ": " + lab[i] + "\n"
        pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)

#Function to get the full name of the month
def getMonthNum(month):
    if month == "Jan":
        return "Gener"
    if month == "Feb":
        return "Febrer"
    if month == "Mar":
        return "Març"
    if month == "Apr":
        return "Abril"
    if month == "May":
        return "Maig"
    if month == "Jun":
        return "Juny"
    if month == "Jul":
        return "Juliol"
    if month == "Aug":
        return "Agost"
    if month == "Sep":
        return "Setembre"
    if month == "Sept":
        return "Setembre"
    if month == "Oct":
        return "Octubre"
    if month == "Nov":
        return "Novembre"
    if month == "Dec":
        return "Desembre"
    return 0

#TITTLE PAGE
pdf.add_page() #Adds a new page
title_page()
#INDEX PAGE
pdf.add_page() #Adds a new page
header()
footer()
#INTRODUCTION
pdf.add_page() #Adds a new page
header()
footer()
pdf.set_margins(26.1, 23.3, 26.1) #Sets the margins
pdf.set_xy(26.1, 23.3)
pdf.set_font('Arial', '', 16) #Sets the font and its style and size
pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
text = "1.- Introducció"
link = pdf.add_link()
pdf.set_link(link, pdf.get_y() , pdf.page_no())
indexLinks.append(link)
indexPages.append(pdf.page_no())
pdf.cell(w=0, h=10, txt=text, border=0, ln=2, align='L')
pdf.set_font('Arial', '', 13) #Sets the font and its style and size
text = "1.1.- Descripció"
link = pdf.add_link()
pdf.set_link(link, pdf.get_y() , pdf.page_no())
indexLinks.append(link)
indexPages.append(pdf.page_no())
pdf.cell(w=0, h=5, txt=text, border=0, ln=2, align='L')
pdf.set_font('Arial', '', 11) #Sets the font and its style and size
pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
text = "El present document descriu la topologia realitzada amb la configuració " + name + " a la empresa TecnoCampus."
pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
pdf.ln(3)
pdf.set_font('Arial', '', 13) #Sets the font and its style and size
pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
text = "1.2.- Objectius"
link = pdf.add_link()
pdf.set_link(link, pdf.get_y() , pdf.page_no())
indexLinks.append(link)
indexPages.append(pdf.page_no())
pdf.cell(w=0, h=5, txt=text, border=0, ln=2, align='L')
pdf.set_font('Arial', '', 11) #Sets the font and its style and size
pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
text = "L’objectiu d’aquest document és la de formalitzar el traspàs d’informació al equip tècnic responsable del manteniment de les infraestructures instal·lades. Aquesta informació fa referencia al disseny, instal·lació i configuració dels dispositius i sistemes afectats per la implementació.\nLa present documentació inclou:\n   - Descripció general de les infraestructures instal·lades.\n   - Configuració de les interfícies de xarxa.\n   - Configuració de les polítiques per les connexions VPN.\n   - Configuració dels protocols d’enrutament.\n   - Configuració de les llistes de control d’accés.\n   - Configuració dels banners."
pdf.multi_cell(w=0, h=5, txt=text.replace(u"\u2019", "'"), border=0, align='J', fill=False)
pdf.ln(3)
pdf.set_font('Arial', '', 13) #Sets the font and its style and size
pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
text = "1.3.- Descripció General de les infraestructures"
link = pdf.add_link()
pdf.set_link(link, pdf.get_y() , pdf.page_no())
indexLinks.append(link)
indexPages.append(pdf.page_no())
pdf.cell(w=0, h=5, txt=text, border=0, ln=2, align='L')
pdf.set_font('Arial', '', 11) #Sets the font and its style and size
pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
text = "Actualment la topologia té la següent distribució:"
pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
pdf.ln(3)
#Generates the graph
G = nx.DiGraph()
for x in links:
    x["id"] #Counts number of links
    n1=x["n1"]
    n1 = n1[1]
    n2=x["n2"]
    n2 = n2[1]
    G.add_edge(label[int(n1)-1],label[int(n2)-1])
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=800)
nx.draw_networkx_edges(G, pos, edgelist = G.edges(),edge_color='black')
nx.draw_networkx_labels(G, pos)
plt.subplots_adjust(top=1, bottom=0.1)
plt.savefig("graph.png")
pdf.image('graph.png', x=60, w=85)
pdf.set_font('Arial', '', 11) #Sets the font and its style and size
pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
text = "En aquesta topologia tenim " + str(len(nodes)) + " equips, connectats a través de " + str(len(links)) + " links."
pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
pdf.ln(3)
#DEVICES CONFIGURATION
pdf.set_font('Arial', '', 16) #Sets the font and its style and size
pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
text = "2.- Configuració dels dispositius"
link = pdf.add_link()
pdf.set_link(link, pdf.get_y() , pdf.page_no())
indexLinks.append(link)
indexPages.append(pdf.page_no())
pdf.cell(w=0, h=7, txt=text, border=0, ln=2, align='L')
pdf.set_font('Arial', '', 11) #Sets the font and its style and size
pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
text = "A continuació, es detalla la configuració dels diferents dispositius:"
pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
pdf.ln(3)
for device in range(len(nodes)):
    partCounter = 1
    string = conf[device]
    pdf.set_font('Arial', '', 13) #Sets the font and its style and size
    pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
    text = "2." + str(device + 1) + ".- " + label[device]
    link = pdf.add_link()
    pdf.set_link(link, pdf.get_y() , pdf.page_no())
    indexLinks.append(link)
    indexPages.append(pdf.page_no())
    pdf.cell(w=0, h=5, txt=text, border=0, ln=2, align='L')
    pdf.ln(2)
    #Get configuration
    if "configuration change" in string: #If the device has configuration
        pdf.ln(-2)
        posChange = string.find("change") + 10
        endChange = string.find("\n!\nversion")
        changeDate = string[posChange:endChange]
        pdf.set_font('Arial', '', 11) #Sets the font and its style and size
        pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
        text = "El darrer canvi de la configuració va ser el " + changeDate[24:28] + " de " + getMonthNum(changeDate[17:20]) + " del " + changeDate[21:23] + " a les " + changeDate[0:12] + "."
        pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
        pdf.ln(3)
        pdf.set_font('Arial', '', 13) #Sets the font and its style and size
        pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
        text = "2." + str(device + 1) + "." + str(partCounter) + ".- Configuració criptogràfica del dispositiu"
        link = pdf.add_link()
        pdf.set_link(link, pdf.get_y() , pdf.page_no())
        indexLinks.append(link)
        indexPages.append(pdf.page_no())
        partCounter+=1
        pdf.cell(w=0, h=5, txt=text, border=0, ln=2, align='L')
        pdf.set_font('Arial', '', 11) #Sets the font and its style and size
        pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
        if "crypto" in string: #If the device has crypto configuration
            text = "El dispositiu té la següent configuració de crypto:\n"
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            text = "   -  Connexió amb " + string[string.find("address") + 8:string.find("\n!\n!\ncrypto ipsec")] + ":"
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            text = "          o  Política de regles número " + string[string.find("policy") + 7:string.find("\n encr")] + ":"
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            text = "                    >  Encriptació " + string[string.find("encr ") + 5:string.find("encr ") + 8] + ", " + string[string.find("encr ") + 9:string.find("\n authentication")]
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            text = "                    >  Autenticació " + string[string.find("\n authentication") + 17:string.find("\n group")]
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            text = "                    >  Diffie-Helmann grup " + string[string.find("\n group") + 8:string.find("\ncrypto isakmp key")]
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            text = "          o  Contrasenya ISAKMP: " + string[string.find("\ncrypto isakmp key") + 18:string.find("address")] + "\n"
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            transformInfo = string[string.find("transform-set") + 14:string.find("\n mode ")]
            text = "          o  Configuració VPN:\n                    >  Conjunt de transformació " + transformInfo[0:transformInfo.find(" ")]
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            transformInfo = transformInfo[transformInfo.find(" ")+1:transformInfo.find("\n")]
            text = "                    >  Configuració Encriptació ESP: " + transformInfo[0:transformInfo.find(" ")]
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            transformInfo = transformInfo[transformInfo.find(" ")+1:transformInfo.find("\n")]
            text = "                    >  Configuració Signatura ESP: " + transformInfo[0:transformInfo.find(" ")]
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            text = "                    >  Mode " + string[string.find("\n mode ") + 7:string.find("\n!\n!\n!\ncrypto map")]
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            text = "                    >  ACL número " + string[string.find("match address") + 14:string.find("\n!\n!\n!\n!\n!\ninterface")]
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
        else: #If the device does not have crypto configuration
            text = "El dispositiu no té configuració crypto.\n"
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
        pdf.ln(3)
        pdf.set_font('Arial', '', 13) #Sets the font and its style and size
        pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
        text = "2." + str(device + 1) + "." + str(partCounter) + ".- Interfícies"
        link = pdf.add_link()
        pdf.set_link(link, pdf.get_y() , pdf.page_no())
        indexLinks.append(link)
        indexPages.append(pdf.page_no())
        partCounter+=1
        pdf.cell(w=0, h=5, txt=text, border=0, ln=2, align='L')
        pdf.set_font('Arial', '', 11) #Sets the font and its style and size
        pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
        text = "Les interfícies i la seva configuració és:\n"
        pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
        getInterfaces(device, string)
        pdf.ln(3)
        pdf.set_font('Arial', '', 13) #Sets the font and its style and size
        pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
        text = "2." + str(device + 1) + "." + str(partCounter) + ".-  Configuració dels protocols d’enrutament"
        link = pdf.add_link()
        pdf.set_link(link, pdf.get_y() , pdf.page_no())
        indexLinks.append(link)
        indexPages.append(pdf.page_no())
        partCounter+=1
        pdf.cell(w=0, h=5, txt=text.replace(u"\u2019", "'"), border=0, ln=2, align='L')
        pdf.set_font('Arial', '', 11) #Sets the font and its style and size
        pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
        if "router" in string:
            text = "El protocol d’enrutament utilitzat és " + string[string.find("router") + 7:string.find("\n network")].upper() + ", amb la següent configuració (xarxes publicades):\n"
            pdf.multi_cell(w=0, h=5, txt=text.replace(u"\u2019", "'"), border=0, align='J', fill=False)
            router = string[string.find(" network"):string.find("area 0\n!") + 6].split(" ")
            networks = []
            for x in router:
                if x != "network" and x!= "area" and x != "0\n" and x!= "0" and x!= "":
                    networks.append(x)
            text = "   -  Àrea " + string[string.find("area") + 5:string.find("area") + 6] + ":"
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            for x in range(len(networks)):
                if x%2==0:
                    text = "          o  Xarxa " + networks[x] + " màscara invertida " + networks[x + 1]
                    pdf.cell(w=0, h=5, txt=text, border=0, ln=0, align='L', fill=False)
                    pdf.ln(5)
        else:
            text = "No s’utilitza protocol d’enrutament."
            pdf.multi_cell(w=0, h=5, txt=text.replace(u"\u2019", "'"), border=0, align='J', fill=False)
        pdf.ln(3)
        pdf.set_font('Arial', '', 13) #Sets the font and its style and size
        pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
        text = "2." + str(device + 1) + "." + str(partCounter) + ".-  Configuració de Llistes de Control d’Accés"
        link = pdf.add_link()
        pdf.set_link(link, pdf.get_y() , pdf.page_no())
        indexLinks.append(link)
        indexPages.append(pdf.page_no())
        partCounter+=1
        pdf.cell(w=0, h=5, txt=text.replace(u"\u2019", "'"), border=0, ln=2, align='L')
        pdf.set_font('Arial', '', 11) #Sets the font and its style and size
        pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
        acl = string[string.find("access-list"):string.find("!\ncontrol-plane") - 1].split(" ")
        if acl[0] == '':
            text = "El dispositiu no té configurada cap ACL."
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
        else:
            text = "El dispositiu té configurada la següent ACL:\n"
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            for x in acl:
                if x != '' and '.' not in x:
                    acl.remove(x)
            text = "   -  Número " + acl[0] + ":\n"
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            text = "          o  PERMIT (" + acl[1] + "):\n"
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            text = "                    >  ORIGEN: " + acl[2] + " màscara invertida " + acl[3] + "\n"
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
            text = "                    >  DESTÍ: " + acl[4] + " màscara invertida " + acl[5] + "\n"
            pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
        pdf.ln(3)
        pdf.set_font('Arial', '', 13) #Sets the font and its style and size
        pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
        text = "2." + str(device + 1) + "." + str(partCounter) + ".-  Configuració de Banners"
        link = pdf.add_link()
        pdf.set_link(link, pdf.get_y() , pdf.page_no())
        indexLinks.append(link)
        indexPages.append(pdf.page_no())
        partCounter+=1
        pdf.cell(w=0, h=5, txt=text, border=0, ln=2, align='L')
        pdf.set_font('Arial', '', 11) #Sets the font and its style and size
        pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
        text = "El dispositiu té configurats els següent Banners:\n"
        pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
        pdf.ln(3)
        text = string[string.find("banner"):string.find("!\nline") - 1].replace("banner", "   -  ").replace("^CCC", "").replace("^C", "")
        pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
    elif string == '' or "# this is a shell script" in string: #If the device does not have configuration
        pdf.set_font('Arial', '', 13) #Sets the font and its style and size
        pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
        text = "2." + str(device + 1) + "." + str(partCounter) + ".- Interfícies"
        link = pdf.add_link()
        pdf.set_link(link, pdf.get_y() , pdf.page_no())
        indexLinks.append(link)
        indexPages.append(pdf.page_no())
        partCounter+=1
        pdf.cell(w=0, h=5, txt=text, border=0, ln=2, align='L')
        pdf.set_font('Arial', '', 11) #Sets the font and its style and size
        pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
        text = "Les interfícies i la seva configuració és:\n"
        pdf.multi_cell(w=0, h=5, txt=text, border=0, align='J', fill=False)
        getInterfaces(device, string)
        pdf.ln(3)
    #Everytime there's a page break, adds a new page with it's header and footer
    if pdf.get_y() > 260:
        pdf.add_page() #Adds a new page
        header()
        footer()
        pdf.set_margins(26.1, 23.3, 26.1) #Sets the margins
        pdf.set_xy(26.1, 23.3)
#INTERFACES
pdf.set_font('Arial', '', 16) #Sets the font and its style and size
pdf.set_text_color(46, 83, 149) #Sets the color of the text (dark blue)
text = "3.- Interfícies"
link = pdf.add_link()
pdf.set_link(link, pdf.get_y() , pdf.page_no())
indexLinks.append(link)
indexPages.append(pdf.page_no())
pdf.cell(w=0, h=5, txt=text, border=0, ln=2, align='L')
pdf.set_font('Arial', '', 11) #Sets the font and its style and size
pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
text = "La configuració de les interfícies (links) d’interconnexió entre equips és:"
pdf.cell(w=0, h=5, txt=text.replace(u"\u2019", "'"), ln=2, align='L')
links = f["links"]
for x in links:
    pdf.ln(5)
    pdf.set_font('Arial', 'B', 11) #Sets the font and its style and size
    text = "   -  Link " + x["id"] + ":"
    pdf.cell(w=0, h=0, txt=text.replace(u"\u2019", "'"), ln=2, align='L')
    n1 = x["n1"]
    n1 = n1[1]
    n2 = x["n2"]
    n2 = n2[1]
    pdf.set_font('Arial', '', 11) #Sets the font and its style and size
    text = "                    connecta " + x["i1"] + " (" + label[int(n1)-1] + ") amb " + x["i2"] + " (" + label[int(n2)-1] + ")"
    pdf.cell(w=0, h=0, txt=text.replace(u"\u2019", "'"), ln=2, align='L')
#Interfaces Table
pdf.ln(-10)
epw = pdf.w - 2*pdf.l_margin
col_width = epw/7
data = [['Xarxa','Equip1','Interfície1','IP1','Equip2','Interfície2','IP2'],
['J10.1.1.0','iosv2','i1','10.1.1.1','iosv1','i2','10.1.1.2'],
['10.2.2.0','iosv2','i3','10.2.2.1','iosv3','i1','10.2.2.2'],[
'192.168.1.0','iosv1','i1','192.168.1.1','alpine-a','i0','192.168.1.3'],[
'192.168.2.0','iosv2','i2','192.168.2.1','alpine-b','i0','192.168.2.3'],[
'192.168.3.0','iosv3','i2','192.168.3.1','alpine-c','i0','192.168.3.3']]
th = pdf.font_size # Text height is the same as current font size
pdf.ln(4*th) # Line break equivalent to 4 lines
pdf.set_font('Arial','B',14.0) 
pdf.cell(epw, 0.0,border=0, align='C')
pdf.set_font('Arial','',10.0) 
pdf.ln(0.5)
pdf.set_draw_color(0,0,0) 
#Here we add more padding by passing 2*th as height
for row in data:
    for datum in row:
        # Enter data in colums
        pdf.set_line_width(1)
        pdf.cell(col_width, 2*th, str(datum), border=1)
    pdf.ln(2*th)
#INDEX
nPage = pdf.page_no() #Returns the current page number
pdf.page = 2 #Go to page (x)
pdf.set_margins(26.1, 23.3, 26.1) #Sets the margins
pdf.set_xy(26.1, 23.3)
pdf.set_font('Arial', '', 11) #Sets the font and its style and size
pdf.set_text_color(0, 0, 0) #Sets the color of the text (black)
sep='   '
text = "1.- Introducció.........................................................................................................................." 
pdf.cell(w=0, h=0, txt=text, border=0, ln=0, align='L', link = indexLinks[0])
text = str(indexPages[0])
pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
pdf.ln(5)
text = sep+"1.1.- Descripció....................................................................................................................." 
pdf.cell(w=0, h=0, txt=text, border=0, ln=0, align='L', link = indexLinks[1])
text = str(indexPages[1])
pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
pdf.ln(5)
text = sep+"1.2.- Objectius......................................................................................................................." 
pdf.cell(w=0, h=0, txt=text, border=0, ln=0, align='L', link = indexLinks[2])
text = str(indexPages[2])
pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
pdf.ln(5)
text = sep+"1.3.- Descripció General de les infraestructures..................................................................."
pdf.cell(w=0, h=0, txt=text, border=0, ln=0, align='L', link = indexLinks[3])
text = str(indexPages[3])
pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
pdf.ln(5)
text = "2.- Configuració dels dispositius.............................................................................................."
pdf.cell(w=0, h=0, txt=text, border=0, ln=0, align='L', link = indexLinks[4])
text = str(indexPages[4])
pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
pdf.ln(5)
count = 1
count2 = 1
linkCount = 5
for x in nodes:
    text = sep + '2.' + str(count) + ".-" + x["label"] +"....................................................................................................."
    pdf.cell(w=0, h=0, txt=text, border=0, ln=0, align='L', link = indexLinks[linkCount])
    text = str(indexPages[linkCount])
    pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
    pdf.ln(5)
    count2=1
    linkCount+=1
    txt = x["label"]
    if "configuration change" in x['configuration']:
        text = sep+sep+'2.'+str(count)+"."+str(count2)+".-Configuració criptogràfica del dispositiu.................................................................."
        pdf.cell(w=0, h=0, txt=text, border=0, ln=0, align='L', link = indexLinks[linkCount])
        text = str(indexPages[linkCount])
        pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
        pdf.ln(5)
        count2+=1
        linkCount+=1
    if x["interfaces"]!="":
        text = sep+sep+'2.'+str(count)+"."+str(count2)+".-Interfícies................................................................................................................."
        pdf.cell(w=0, h=0, txt=text, border=0, ln=0, align='L', link = indexLinks[linkCount])
        text = str(indexPages[linkCount])
        pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
        pdf.ln(5)
        count2+=1
        linkCount+=1
    if "configuration change" in x['configuration']:
        text = sep+sep+'2.'+str(count)+"."+str(count2)+".-Configuració dels protocols d'enrutament..............................................................."
        pdf.cell(w=0, h=0, txt=text, border=0, ln=0, align='L', link = indexLinks[linkCount])
        text = str(indexPages[linkCount])
        pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
        pdf.ln(5)
        count2+=1
        linkCount+=1
        text = sep+sep+'2.'+str(count)+"."+str(count2)+".-Configuració de Llistes de Control d'Accés............................................................."
        pdf.cell(w=0, h=0, txt=text, border=0, ln=0, align='L', link = indexLinks[linkCount])
        text = str(indexPages[linkCount])
        pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
        pdf.ln(5)
        count2+=1
        linkCount+=1
        text = sep+sep+'2.'+str(count)+"."+str(count2)+".-Configuració de Banners........................................................................................."
        pdf.cell(w=0, h=0, txt=text, border=0, ln=0, align='L', link = indexLinks[linkCount])
        text = str(indexPages[linkCount])
        pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
        pdf.ln(5)
        count2+=1
        linkCount+=1
    count+=1
text ="3.- Interfícies............................................................................................................................"
pdf.cell(w=0, h=0, txt=text, border=0, ln=0, align='L', link = indexLinks[linkCount])
text = str(indexPages[linkCount])
pdf.cell(w=0, h=0, txt=text, border=0, ln=2, align='L')
pdf.ln(5)
pdf.page = nPage #Go to page (x)

name = name + ".pdf"
pdf.output(name, 'F') #Creates the pdf file
print(name + " created")