#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import sdf, json
from converter.SDFExtension import SDFExtension
from scipy.io import loadmat
class Test(unittest.TestCase):


    '''def test_xlsx_sdf(self):
        print 'xlsx'
        sdf_ext = SDFExtension()
        sdf_ext.load_data('cycleTemplateError.xlsx', 'xlsx')
        sdf_ext.save_to_file('out_cycleTemplate.sdf', 'sdf')
    '''    
    
    def test_mat_sdf(self):    
        print 'mat'
        sdf_ext = SDFExtension(True)
        
        sdf_ext.load_data('cycleTemplate.sdf', 'sdf')
        
        sdf_ext1 = SDFExtension()
        sdf_ext1.load_data('cycleTemplateError.xlsx', 'xlsx')
        
        sdf_ext1.set_schema_data(sdf_ext)
        sdf_ext1.validate()
        sdf_ext1.save_to_file('out_csample.sdf', 'sdf')
    '''    
    def test_sdf_sdf(self):
        print 'sdf'
        sdf_ext = SDFExtension()
        sdf_ext.load_data('cycleTemplate.sdf', 'sdf')
        sdf_ext.save_to_file('out_cycleTemplate1.sdf', 'sdf')   

    def test_xlsx_mat(self):
        print 'xlsx to mat'
        sdf_ext = SDFExtension()
        sdf_ext.load_data('cycleTemplate.xlsx', 'xlsx')
        sdf_ext.save_to_file('out_cycleTemplate1.mat', 'mat')  
        print loadmat('out_cycleTemplate1.mat')
        
    def test_xlsx_xlsx(self):
        print 'xlsx to xlsx'
        sdf_ext = SDFExtension()
        sdf_ext.load_data('cycleTemplate.xlsx', 'xlsx')
        sdf_ext.save_to_file('out_cycleTemplate1.xlsx', 'xlsx')  

    def test_mat_mat(self):
        print 'mat to mat'
        sdf_ext = SDFExtension()
        sdf_ext.load_data('out_cycleTemplate1.mat', 'mat')
        sdf_ext.save_to_file('out_cycleTemplate2.mat', 'mat')
        print loadmat('out_cycleTemplate1.mat')  
        print loadmat('out_cycleTemplate2.mat')
        '''

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    