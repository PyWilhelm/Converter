#!/usr/bin/python
# -*- coding: utf-8 -*-
import sdf, os, sys
from converter.load_file import load_from_sdf, load_from_mat, load_from_xlsx
from converter.save_file import save_to_sdf, save_to_mat, save_to_xlsx
from validater import Validater

reload(sys)
# The utf-8 characters (äöü) should be saved in the input and output formats
sys.setdefaultencoding("utf-8")

class SDFExtension(object):

    def __init__(self, is_schema=False):
        self.__dataset_list = []
        self.__schema_data = None
        self.__is_schema = is_schema
        
    def get_schema(self):
        return self.__schema_data
    
    def __getitem__(self, name):
        temp_list = [ds for ds in self.__dataset_list if ds.name == name]
        if len(temp_list) == 0:
            return None
        else:
            return temp_list[0]
        
    def keys(self):
        return [ds.name for ds in self.__dataset_list]
    
    def load_data(self, input_filename, format_string):   # format: 'sdf', 'mat', 'xlsx'
        load_function = self.__get_load_function(format_string) # not handle padding routine
        if self.__schema_data != None and format_string.find('mat') >= 0:
            dataset_list = load_function(input_filename, self.__schema_data)
        else: 
            dataset_list = load_function(input_filename)

        if self.__is_schema:
            self.__dataset_list = self.__clear_data(dataset_list)
        else:
            self.__dataset_list = dataset_list

        
        
    def __clear_data(self, dataset_list):
        for ds in dataset_list:
            ds.data = []
        return dataset_list
    
    def __get_load_function(self, format_string):
        if format_string.find('sdf') >= 0:
            return load_from_sdf
        elif format_string.find('xls') >= 0:
            return load_from_xlsx
        elif format_string.find('mat') >= 0:
            return load_from_mat
            
    def __get_save_function(self, format_string):
        if format_string.find('sdf') >= 0:
            return save_to_sdf
        elif format_string.find('xls') >= 0:
            return save_to_xlsx
        elif format_string.find('mat') >= 0:
            return save_to_mat
        
    def set_scale(self):
        time_ds = self.__getitem__('time')
        for ds in self.__dataset_list:
            if ds.name != 'time':
                ds.scales = [time_ds]
        
    def validate(self):
        report_syntax = self.__syntax_validate()
        report_semantic = self.__semantic_validate()
        return report_syntax, report_semantic
        
    def save_to_file(self, filename, file_format):
        save_function = self.__get_save_function(file_format)
        save_successful = save_function(self.__dataset_list, filename)
        return save_successful
    
    def __syntax_validate(self):
        vali = Validater.validate_syntax(self)
        print str(vali)
    
    def __semantic_validate(self):
        vali = Validater.validate_semantic(self)
        print str(vali)
    
    def __save(self, filename, file_format):
        return True
        
    
    def set_schema_data(self, schema_sdf_ext):
        self.__schema_data = schema_sdf_ext
        
