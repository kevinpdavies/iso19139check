#!/usr/bin/env python
from __future__ import print_function
import lxml.etree as etree 
import uuid
import datetime
import gdal
import argparse
import os.path

ns = {
    'gco': 'http://www.isotc211.org/2005/gco',
    'gmd': 'http://www.isotc211.org/2005/gmd',
}

def go(xml_file):
    
    print("Validating", xml_file)
    # Setup the parser and open the file
    schema_root = etree.parse(os.path.dirname(__file__) + \
        "/iso19139.anzlic/schema/gmd/gmd.xsd")
    schema = etree.XMLSchema(schema_root)
    parser = etree.XMLParser(schema = schema)
    tree = etree.parse(xml_file, parser)
    print("Validation OK")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(\
        description='Validate ISO19139 metadata file against the schema.')
    parser.add_argument("xml_file", help="ISO19139 metadata XML file")
    
    args = parser.parse_args()
    go(args.xml_file)
