import xml.etree.cElementTree as arbol

buzones = []
with open('buzones.txt', 'r') as ficheroBuzones:
    for line in ficheroBuzones:
        if '&' in line:
            line.replace('&','&amp;')
        buzones.append(line.decode('utf-8').rstrip())

propietarios = []
with open('propietarios.txt','r') as ficheroPropietarios:
    for line in ficheroPropietarios:
        propietarios.append(line.rstrip())

backups = []
with open('backups.txt', 'r') as ficheroBackups:
    for line in ficheroBackups:
        backups.append(line.rstrip())

raizXML = arbol.Element("owners_list")
tipo = arbol.SubElement(raizXML,"request_type")
nombre = arbol.SubElement(tipo,"name")
nombre.text = "Mailbox"
for i in range(0, len(buzones)):
    subtipo = arbol.SubElement(tipo, "request_subtype")
    buzon = arbol.SubElement(subtipo, "name")
    buzon.text = buzones[i]
    propietario = arbol.SubElement(subtipo, "owner_id")
    propietario.text = propietarios[i]
    backup = arbol.SubElement(subtipo, "backup_id")
    backup.text = backups[i]

estructuraFinal = arbol.ElementTree(raizXML)
estructuraFinal.write("Mailbox_Owners.xml",encoding="UTF-8",xml_declaration=True)
