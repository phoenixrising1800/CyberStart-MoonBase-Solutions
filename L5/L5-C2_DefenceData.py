# ""Defence Data"
# Generate a valid xml file at /tmp/vulnerable-countries.xml.
# It should contain a list of country nodes attached to a root node.
# Each country node should have a name attribute.
# The third node name should be Panama.
#
import xml.etree.cElementTree as ET

myfile = '/tmp/vulnerable-countries.xml'
root = ET.Element("root")
ET.SubElement(root, "country", name="Iran")
ET.SubElement(root, "country", name="Antarctica")
ET.SubElement(root, "country", name="Panama")
tree = ET.ElementTree(root)
tree.write(myfile)
