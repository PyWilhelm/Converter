#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from converter.SDFExtension import SDFExtension
def converter_file(queue, inputfile, schemafile, outputfile):
    get_format = lambda filepath: filepath[filepath.rfind('.')+1:]
    sdf_ext_schema = SDFExtension(True)
    sdf_ext_schema.load_data(schemafile, get_format(schemafile))
    
    sdf_ext = SDFExtension()
    sdf_ext.set_schema_data(sdf_ext_schema)
    sdf_ext.load_data(inputfile, get_format(inputfile))
    syntax, semantic = sdf_ext.validate()
    sdf_ext.save_to_file(outputfile, get_format(outputfile))
    queue.put((syntax, semantic))
    return (syntax, semantic)
    
def template_get_muster_list(schemafile):
    get_format = lambda filepath: filepath[filepath.rfind('.')+1:]
    sdf_ext_schema = SDFExtension(True)
    sdf_ext_schema.load_data(schemafile, get_format(schemafile))
    return sdf_ext_schema.get_first_muster_list(), sdf_ext_schema

def template_generate(sdf_ext_schema, outputfile, muster_value_list):
    muster_name_list = sdf_ext_schema.get_first_muster_list()
    muster_dict = {muster_name_list[i]: muster_value_list[i] for i in range(len(muster_value_list))}
    get_format = lambda filepath: filepath[filepath.rfind('.')+1:]
    sdf_ext_schema.save_template_to_file(outputfile, get_format(outputfile), muster_dict)