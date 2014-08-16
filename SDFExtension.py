#!/usr/bin/python
# -*- coding: utf-8 -*-
import sdf

class SDFExtension(object):

    def __init__(self, is_schema=False):
        self.__dataset_list = []
        self.__schema_data = None
        self.__is_schema = is_schema
        
    
    def __getitem__(self, name):
        temp_list = [ds for ds in self.__dataset_list if ds.name == name]
        if len(temp_list) == 0:
            return None
        else:
            return temp_list[0]
        
    def keys(self):
        return [ds.name for ds in self.__dataset_list]
    
    def load_data(self, data, format):   # format: 'sdf', 'mat', 'xlsx'
        # TODO: 
        dataset_list = data
        # 
        if self.__is_schema:
            self.__dataset_list = self.__clear_data(dataset_list)
        else:
            self.__dataset_list = dataset_list
        
    def __clear_data(self, dataset_list):
        for ds in dataset_list:
            ds.data = []
        return dataset_list
    
    def save_to_file(self, filename, file_format):
        report_syntax = self.__syntax_validate()
        report_semantic = self.__semantic_validate()
        # TODO: save to file system
        save_successful = self.__save(filename, file_format)
        return save_successful, report_syntax, report_semantic
    
    def __syntax_validate(self):
        # TODO:
        return ValidateReport()
    
    def __semantic_validate(self):
        # TODO:
        return ValidateReport()
    
    def __save(self, filename, file_format):
        return True
        
    
    def set_schema_data(self, schema_sdf_ext):
        self.__schema_data = schema_sdf_ext
        
class ValidateReport(object):    
    pass