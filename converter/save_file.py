#!/usr/bin/python
# -*- coding: utf-8 -*-
import sdf, lib
from scipy.io import savemat
import xlsxwriter
def save_to_sdf(dataset_list, output_filename):
    group = sdf.Group('/', comment='converted file', datasets = dataset_list)
    sdf.save(output_filename, group)
    
def save_to_mat(dataset_list, output_filename):
    mat_dict = {ds.name: ds.data for ds in dataset_list}
    savemat(output_filename, mdict=mat_dict, format='4')
    
def save_to_xlsx(dataset_list, output_filename):
    names = [ds.name for ds in dataset_list]
    prefix_list = reduce(lib.get_prefix, names, [])
    dataset_of_prefix = {p: [ds for ds in dataset_list if ds.name.find(p)>=0]for p in prefix_list}
    workbook = xlsxwriter.Workbook(output_filename)
    keys = ['time'] + sorted([key for key in dataset_of_prefix.keys() if key != 'time'])
    for key in keys:
        worksheet = workbook.add_worksheet(key)
        try:
            __write_to_sheet(workbook, worksheet, dataset_of_prefix[key])
        except:
            pass
            
    workbook.close()
         
    
def __write_to_sheet(workbook, worksheet, dataset_list):
    f1 = __get_header_format(workbook)
    f2 = __get_string_format(workbook)
    worksheet.write('A1', 'name', f1)
    worksheet.write('A2', 'quantity', f1)
    worksheet.write('A3', 'unit', f1)
    worksheet.write('A4', 'comment', f1)
    #TODO: extract all the names which share a same prefix into a list
    # write the data in a sheet
    for i, ds in enumerate(dataset_list):
        print ds
        worksheet.write(0, i+1, ds.name, f2)
        worksheet.write(1, i+1, ds.quantity, f2)
        worksheet.write(2, i+1, ds.unit, f2)
        worksheet.write(3, i+1, ds.comment, f2)
        for data_index, value in enumerate(ds.data):
            worksheet.write(data_index+4, i+1, value)

def __get_header_format(workbook):
    f = workbook.add_format({'bold': True, 'border': 1})
    f.set_align('top')
    return f

def __get_string_format(workbook):
    f = workbook.add_format({'border': 1, 'text_wrap': True})
    f.set_align('top')
    return f
