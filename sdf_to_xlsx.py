'''


@author: schatz
'''
import os.path
import numpy as np
import sdf
import sys
import xlsxwriter

def create_xlsx_workbook(filename):
    outfile = 'out_'+os.path.splitext(filename)[0]+'.xlsx'
    workbook = xlsxwriter.Workbook(outfile)  #wb1=Workbook()新建立一个工作簿wb1
    return workbook

def load_data(filename):
    #TODO: read the data from sdf using the intermediate data structure
    return sdf_data

def write_time_sheet(workbook, 'time'):
    time_sh = workbook.add_worksheet('time') #ewb1=ExcelWriter(workbook=wb1)#新建一个ExcelWriter，用来写wb1
    time_sh.write('A1', 'name')
    time_sh.write('A2', 'quantity')
    time_sh.write('A3', 'unit')
    time_sh.write('A4', 'comment')
    time_sh.write('B1', ds.name)
    time_sh.write('B2', ds.quantity)
    time_sh.write('B3', ds.unit)
    time_sh.write('B4', ds.comment)
    return time_sheet

def write_to_sheet(workbook, sdf_data):
    #TODO: write the data from the intermediate data structure
    worksheet = sdf_data.name[:str.find('_')]
    worksheet.write('A1', 'name')
    worksheet.write('A2', 'quantity')
    worksheet.write('A3', 'unit')
    worksheet.write('A4', 'comment')
    #TODO: extract all the names which share a same prefix into a list
    # write the data in a sheet
    for i in range(len(list))
        worksheet.write(0, i+1, list[i], name)
        worksheet.write(1, i+1, list[i], quantity)
        worksheet.write(2, i+1, list[i], unit)
        worksheet.write(3, i+1, list[i], comment)

    return other_sheets

def save_to_file(filename, sdf_data):
    #TODO including 'time' table and the other data, may use write_time_sheet() and write_to_sheet()
    # sdf_data = time_sheet + other_sheets

def converter(filename):
    #TODO:s read data from sdf
    workbook = create_xlsx_workbook(filename) # create a new workbook
    sdf_data = load_data(filename)  # get the immediate data from sdf
    save_to_file(filename, sdf_data)   # write the immediate data into xlsx
    workbook.close