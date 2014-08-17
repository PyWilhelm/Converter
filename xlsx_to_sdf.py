'''


@author: schatz
'''
import os.path
import numpy as np
import sdf
import sys
import xlrd
import copy

def load_data(workbook):
    xlsx_data = workbook_dict(workbook)
    return xlsx_data

def time_dict(workbook): # return a time dict data
    time_sheet = workbook.sheet_by_name('time')
    time_name = time_sheet.cell_value(0, 1)
    time_quantity = time_sheet.cell_value(1, 1)
    time_unit = time_sheet.cell_value(2, 1)
    time_comment = time_sheet.cell_value(3, 1)
    time_value = time_sheet.col_values(1, 4, time_sheet.nrows)
#     time_list = []
#     time_list.append(time_name)
#     time_list.append(time_quantity)
#     time_list.append(time_unit)
#     time_list.append(time_comment)
#     time_list.append(time_value)
#     dict_time = {time_list[0]: time_list[1:]}
    dict_time = {time_name : (time_quantity, time_unit, time_comment, time_value) }
    return dict_time

def column_dict(sheet, column, scales): # return a column dict data
    name = sheet.cell_value(0, column)
    quantity = sheet.cell_value(1, column)
    unit = sheet.cell_value(2, column)
    comment = sheet.cell_value(3, column)
    column_data = sheet.col_values(column, 4, sheet.nrows)
    sheet_list = []
    sheet_list.append(name)
    sheet_list.append(quantity)
    sheet_list.append(unit)
    sheet_list.append(comment)
    sheet_list.append(column_data)
    dict_column = {sheet_list[0]: sheet_list[1:]}
    return dict_column

def sheet_dict(sheet, vec_start_row=4):
#     dict_org = column_dict(sheet, 1, scales=None)
#     for column in range(2, sheet.ncols):
#         dict_merge = copy.deepcopy(dict_org)
#         for key, value in column_dict(sheet, column, scales=None).items():
#             dict_merge[key] = value
#             dict_org = dict_merge
#     return dict_org
    sh = sheet#workbook.sheet_by_name(sheet)
    d = {}
    for c in range(1, sh.ncols):
        col_i = [ sh.cell_value(r, c) for r in range(sh.nrows) ]
        # d -> { <col_name> : < ( col_attr1, col_attr2, ... , [ col_data ]  }
        d[col_i[0]] = tuple(col_i[1:vec_start_row]) + (col_i[vec_start_row:],)
    return d

def workbook_dict(workbook):
    wd = {}
    for sheet in workbook.sheets():
        wd.update(sheet_dict(sheet))
    return wd

def convert(xlsx_data):
    '@xlsx_data is the workbook_dict'
    '@xlsx_data is a dict({ <> : <> })'
#
#
#     dict_time = time_dict(xlrd.open_workbook(filename))
#     ds_t = sdf.Dataset(n_t, data=t, quantity=q_t, unit=u_t, is_scale=True, scale_name='time')
#     return sdf_data
    def make_dataset_from_kv_pair(k, v, scale_time):
        return sdf.Dataset(k,
                           quantity=v[0],
                           unit=v[1],
                           comment=v[2],
                           data=np.array(v[3]),
                           is_scale=False,
                           scales=[scale_time])

    time_tuple = xlsx_data[u'time']
    ds_t = sdf.Dataset(u'time',
                       quantity=     time_tuple[0],
                       unit=         time_tuple[1],
                       comment=      time_tuple[2],
                       data=np.array(time_tuple[3]),
                       is_scale=True,
                       scale_name=u'time')
    other_datasets = \
        [ make_dataset_from_kv_pair(sh_k, sh_tp, ds_t)
                for sh_k, sh_tp in xlsx_data.items()
                if sh_k <> u'time' ]
    return [ ds_t ] + other_datasets

def save_to_file(filename):
    ''
    workbook = xlrd.open_workbook(filename)
    xlsx_data = load_data(workbook)
    sdf_data = convert(xlsx_data)
    g = sdf.Group('/', comment='Imported from ' + filename, datasets = sdf_data)
    outfile = os.path.splitext(filename)[0] + '.sdf'
    print outfile
    sdf.save(outfile, g)

def gui_converter():
    return
