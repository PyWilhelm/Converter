#!/usr/bin/python
# -*- coding: utf-8 -*-
import sdf, types,copy, xlrd, numpy
from scipy.io import loadmat

def load_from_sdf(input_filename):
    return sdf.load_all(input_filename, set_scale=False)

def load_from_mat(input_filename, schema_data=None):
    mat_data = loadmat(input_filename)
    try:
        del mat_data['__header__']
        del mat_data['__globals__']
        del mat_data['__version__']
    except:
        pass
    data_list = [sdf.Dataset(key, data=mat_data[key][0].tolist()) for key in mat_data.keys()]
    if schema_data == None:
        return data_list
    else:
        return load_from_mat_padding(data_list, schema_data)
# A padding function should be executed, 
# in order to complete the missing information defined in the schema data, 
# when a source file in the ‘.mat ‘ format is handled
def load_from_mat_padding(dataset_list, schema_data):
    ds_final_list = []
    for ds in dataset_list:
        ds_final = copy.deepcopy(schema_data[ds.name])
        ds_final.data = ds.data
        ds_final_list.append(ds_final)
    return ds_final_list

def load_from_xlsx(input_filename):
    workbook = xlrd.open_workbook(input_filename)
    xlsx_data_list = __get_workbook_dict(workbook)
    return [sdf.Dataset(**data) for data in xlsx_data_list]

    
def __get_sheet_dict(sheet, template_list, vec_start_row=4):
    matrix = [[sheet.cell_value(r, c) for r in range(sheet.nrows)] for c in range(1, sheet.ncols)]
    get_data = lambda ls: [i for i in ls if isinstance(i, types.IntType) or isinstance(i, types.FloatType)]
    data_list = [{template_list[i]: col[i] if i<len(template_list)-1 else numpy.array(get_data(col[i:]))
                  for i in range(len(template_list))} 
                 for col in matrix]
    
    return data_list

def __get_col_template_list(sheet, template_pos=0, vec_start_row=4):
    return [key for key in [sheet.cell_value(r, template_pos) for r in range(sheet.nrows) if r < vec_start_row]] + ['data']

def __get_workbook_dict(workbook):
    return_list = []
    for sheet in workbook.sheets():
        template_list = __get_col_template_list(sheet)
        return_list.extend(__get_sheet_dict(sheet, template_list))
    return return_list
    