from pathlib import Path
import xml.etree.ElementTree as ET


index_import = r'D:\contextupdater\xml_samples\contextDocumentationIndex.xml'
sampleb = r'xml_samples/beginindex.xml'
samplee = r'xml_samples/endindex.xml'

tree = ET.parse(samplee)
root = tree.getroot()

print(ET.tostring(root, encoding='UTF-8', method="xml").decode('UTF-8'))