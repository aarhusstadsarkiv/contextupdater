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
roots = [rootb, root, roote]
xml_element_tree = None
bigtree = ET.ElementTree()

for row in root.findall('.//table_ns:documentID', ns): 
    row.text = int(row.text) + 4
    row.text = str(row.text)
    docid = []
    docid.append(row.text)

for doc in roote.findall('.//table_ns:documentID', ns):
    doc.text = int(docid[-1]) + 1
    doc.text = str(doc.text)

for i in roots:
    if xml_element_tree is None:
        xml_element_tree = i
    else:
        xml_element_tree.extend(i)

bigtree._setroot(xml_element_tree)
#print(ET.tostring(xml_element_tree, encoding='UTF-8', xml_declaration=True, default_namespace=table_ns, method="xml").decode('UTF-8'))
bigtree.write(export_text, encoding="UTF-8", xml_declaration=True, default_namespace=table_ns, method="xml")