import csv
import xml.etree.ElementTree as ET
import re

def sanitize_tag(tag):
    # Reemplaza espacios por guion bajo y elimina caracteres no permitidos
    tag = tag.strip()                   # Quita espacios al inicio/final
    tag = tag.replace(" ", "_")         # Reemplaza espacios por _
    tag = re.sub(r"[^\w\-]", "", tag)  # Elimina caracteres que no sean letras, números o guion/_
    if tag[0].isdigit():                # Si empieza con número, antepone "_"
        tag = "_" + tag
    return tag

def csv_to_xml(csv_file_path, xml_file_path):
    root = ET.Element("data")

    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            item = ET.SubElement(root, "item")
            for key, value in row.items():
                clean_key = sanitize_tag(key)
                child = ET.SubElement(item, clean_key)
                child.text = value

    tree = ET.ElementTree(root)
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

# Ejemplo de uso
csv_file_path = "pruebasimple - Full 1.csv"
xml_file_path = "hola1.xml"
csv_to_xml(csv_file_path, xml_file_path)
print(f"Converted {csv_file_path} to {xml_file_path}")