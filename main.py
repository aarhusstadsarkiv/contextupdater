from pathlib import Path
import xml.etree.ElementTree as ET

index_import = r'xml_samples/contextDocumentationIndex.xml' #change this path to the directory of the contextDocumentationIndex you want to change
sampleb = r'xml_samples/beginindex.xml'
samplee = r'xml_samples/endindex.xml'
export_text = r'xml_samples/new_contextDocumentationIndex.xml' #change this path if you want the new index in another directory

for event, elem in ET.iterparse(Path(index_import), events=['start-ns']): #finds namespace
    if "www.sa.dk" in elem[1]:
        table_ns = elem[1]
ns = {'table_ns': table_ns} #namespaceregister

tree = ET.parse(Path(index_import)) #load XML-files into trees and roots
root = tree.getroot()
treeb = ET.parse(Path(sampleb))
rootb = treeb.getroot()
treee = ET.parse(Path(samplee))
roote = treee.getroot()
roots = [rootb, root, roote] #list of roots
xml_element_tree = None
bigtree = ET.ElementTree() #for combining the trees later
doclist = []
docid = []

for r in rootb.findall('.//table_ns:documentID', ns): #find all documentID's for the first documents
    doclist.append(r.text)

for row in root.findall('.//table_ns:documentID', ns): #change documentID's for the old contextDocumentationIndex
    row.text = int(row.text) + len(doclist)
    row.text = str(row.text)
    docid.append(row.text)

for doc in roote.findall('.//table_ns:documentID', ns): #change documentID for the last document
    doc.text = int(docid[-1]) + 1
    doc.text = str(doc.text)

for i in roots: #combine the three roots into one tree and plant it
    if xml_element_tree is None:
        xml_element_tree = i
    else:
        xml_element_tree.extend(i)
bigtree._setroot(xml_element_tree)
#print(ET.tostring(xml_element_tree, encoding='UTF-8', xml_declaration=True, default_namespace=table_ns, method="xml").decode('UTF-8'))
bigtree.write(export_text, encoding="UTF-8", xml_declaration=True, default_namespace=table_ns, method="xml")