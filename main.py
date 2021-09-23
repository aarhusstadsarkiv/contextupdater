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

#tree.write(export_text, encoding="UTF-8", xml_declaration=True, default_namespace=table_ns, method="xml")
#print(ET.tostring(root, encoding='UTF-8', method="xml").decode('UTF-8'))

for row in root.findall('.//table_ns:documentID', ns):
    row.text = int(row.text) + 4
    row.text = str(row.text)
    docid = []
    docid.append(row.text)
    #print(ET.tostring(root, encoding='UTF-8', method="xml").decode('UTF-8'))
#print(int(docid[-1]) + 1)

for doc in roote.findall('.//table_ns:documentID', ns):
    doc.text = int(docid[-1]) + 1
    doc.text = str(doc.text)
    #print(ET.tostring(roote, encoding='UTF-8', method="xml").decode('UTF-8'))

#merge = [treeb, tree, treee]
#print(ET.tostringlist(merge, encoding='UTF-8', method="xml").decode('UTF-8'))



test = [rootb, root, roote]
'''
def run():
    xml_element_tree = None
    for data in test:
        #print(ET.tostring(data, encoding='UTF-8', xml_declaration=True, default_namespace=table_ns, method="xml").decode('UTF-8'))
        for result in data.iter():
            if xml_element_tree is None:
                xml_element_tree = result
                #insertion_point = xml_element_tree.findall("./table_ns:document", ns)[0]
            else:
                xml_element_tree.extend(result) 
    if xml_element_tree is not None:
        #print(ET.tostring(xml_element_tree, encoding='UTF-8', xml_declaration=True, default_namespace=table_ns, method="xml").decode('UTF-8'))
        #print("Tree is not none")
        return xml_element_tree

xml_element_tree = run()'''

'''
def combine_xml(files):
    first = None
    for filename in files:
        data = ET.parse(filename).getroot()
        if first is None:
            first = data
        else:
            first.extend(data)
    if first is not None:
        return ET.tostring(first)'''



#for scrap in xml_element_tree.findall(".", ns):
    #print(ET.tostring(scrap, encoding='UTF-8', xml_declaration=True, default_namespace=table_ns, method="xml").decode('UTF-8'))


#bigtree = ET.ElementTree()
#bigtree._setroot(xml_element_tree)
#print(ET.tostring(xml_element_tree, encoding='UTF-8', xml_declaration=True, default_namespace=table_ns, method="xml").decode('UTF-8'))
#bigtree.write(export_text, encoding="UTF-8", xml_declaration=True, default_namespace=table_ns, method="xml")



#for element in test:
#    with open(export_text, "a") as append_file:
#        append_file.write(ET.tostring(element, encoding='UTF-8', xml_declaration=True, default_namespace=table_ns, method="xml").decode('UTF-8'))

#for lol in merge:
#    #print(ET.tostring(lol.getroot(), encoding='UTF-8', method="xml").decode('UTF-8'))
#    lol.write(export_text, encoding="UTF-8", xml_declaration=True, default_namespace=table_ns, method="xml")