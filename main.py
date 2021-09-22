from pathlib import Path
import xml.etree.ElementTree as ET


index_import = r'D:\contextupdater\xml_samples\contextDocumentationIndex.xml'
sampleb = r'xml_samples/beginindex.xml'
samplee = r'xml_samples/endindex.xml'
export_text = r'xml_samples/test.xml'

for event, elem in ET.iterparse(Path(index_import), events=['start-ns']): #finder namespace
    if "www.sa.dk" in elem[1]:
        table_ns = elem[1]
ns = {'table_ns': table_ns} #namespaceregister

tree = ET.parse(Path(index_import))
root = tree.getroot()
treeb = ET.parse(Path(sampleb))
rootb = treeb.getroot()
treee = ET.parse(Path(samplee))
roote = treee.getroot()

tree.write(export_text, encoding="UTF-8", xml_declaration=True, default_namespace=table_ns, method="xml")
#print(ET.tostring(root, encoding='UTF-8', method="xml").decode('UTF-8'))

for row in root.findall('.//table_ns:documentID', ns):
    row.text = int(row.text) + 4
    row.text = str(row.text)
    #print(ET.tostring(root, encoding='UTF-8', method="xml").decode('UTF-8'))


#merge = [treeb, tree, treee]
#print(ET.tostring(merge, encoding='UTF-8', method="xml").decode('UTF-8'))
'''
test = [rootb, root, roote]
for element in test:
    with open(export_text, "a") as append_file:
        append_file.write(ET.tostring(element, encoding='UTF-8', xml_declaration=True, default_namespace=table_ns, method="xml").decode('UTF-8'))

for lol in merge:
    #print(ET.tostring(lol.getroot(), encoding='UTF-8', method="xml").decode('UTF-8'))
    lol.write(export_text, encoding="UTF-8", xml_declaration=True, default_namespace=table_ns, method="xml")'''