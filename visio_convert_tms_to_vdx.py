#!/usr/bin/python
from xml.etree import ElementTree
import sys

if len(sys.argv) == 1:
    print "[*] Usage: ./script <some .tms file> <output file name>"
    sys.exit(1)

with open(sys.argv[1]) as f:
    root = ElementTree.parse(f)
    print root.find("VisioFile")

    output_name = sys.argv[2]
    if not output_name.endswith(".vdx"):
        output_name += ".vdx"

    with open(output_name, "w") as g:
        text = root.find("VisioFile").text
        text = text.replace("&gt;", ">")
        text = text.replace("&amp;", "&")
        g.write(text)
