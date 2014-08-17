#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, lib, copy
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

    def set_scale(self):
        time_ds = self.__getitem__('time')
        for ds in self.__dataset_list:
            if ds.name != 'time':
                ds.scales = [time_ds]
        
    def set_schema_data(self, schema_sdf_ext):
        self.__schema_data = schema_sdf_ext
        
    def validate(self):
        report_syntax = self.__syntax_validate()
        report_semantic = self.__semantic_validate()
        self.set_scale()
        return report_syntax, report_semantic
        
    def save_to_file(self, filename, file_format):
        save_function = self.__get_save_function(file_format)
        save_successful = save_function(self.__dataset_list, filename)
        return save_successful  
    
    def get_first_muster_list(self):
        if self.__is_schema == True:
            first_muster_dict = lib.get_first_muster_dict(lib.get_dataset_dict_by_prefix(self))
            return first_muster_dict.keys()
        else:
            raise Exception('the function only for schema data')
        
    def save_template_to_file(self, outputfile, file_format,  muster_dict):
        def rename(ds, key, newkey): 
            ds.name = ds.name.replace(key, newkey)
        sdf_ext = SDFExtension()
        first_muster_dict = lib.get_first_muster_dict(lib.get_dataset_dict_by_prefix(self))
        dataset_list = []
        for key in first_muster_dict.keys():
            for i in range(1, muster_dict[key]+1):
                temp_list = copy.deepcopy(first_muster_dict[key])
                [rename(ds, key+'1', key+str(i)) for ds in temp_list]
                dataset_list.extend(temp_list)
        dataset_list.append(self.__getitem__('time'))
        sdf_ext._set_dataset_list(dataset_list)
        return sdf_ext.save_to_file(outputfile, file_format)
        
    def _set_dataset_list(self, ds_list):
        self.__dataset_list = ds_list
        
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
        

    
    def __syntax_validate(self):
        vali = Validater.validate_syntax(self)
        print 'syntax:'
        print vali
        return vali
    
    def __semantic_validate(self):
        vali = Validater.validate_semantic(self)
        print 'semantic:'
        print vali
        return vali
    
        

        
