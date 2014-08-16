#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import sdf, SDFExtension

class Test(unittest.TestCase):


    def testName(self):
        ds_list = sdf.load_all('cycleTemplate.sdf')
        sdf_ext = SDFExtension.SDFExtension(True)
        sdf_ext.load_data(ds_list, 'sdf')
        for key in sdf_ext.keys():
            print sdf_ext[key].name,'--', sdf_ext[key]


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    