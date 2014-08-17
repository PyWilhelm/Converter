#!/usr/bin/python
# -*- coding: utf-8 -*-

def get_prefix(prefix_list, name):
    number_string_list = [str(i) for i in range(10)]
    return_list = []
    find = False
    for prefix in prefix_list:
        for i in range(len(prefix)):
            if prefix[i] != name[i]:
                prefix_fix = prefix[:i]
                if len(prefix_fix)>1 \
                    and prefix_fix[-1] not in number_string_list \
                    and name != 'time' \
                    and prefix[-1] in number_string_list:   # only number different, e.g. em1 em2
                    prefix_fix += name[len(prefix_fix)]
                    return_list.append(prefix)
                break
        else:
            prefix_fix = prefix
        prefix_fix = prefix_fix.replace('_', '')
        if len(prefix_fix) > 1 :
            find = True
            return_list.append(prefix_fix)
        else:
            return_list.append(prefix)
    if find == False:
        return_list.append(name)
    return list(set(return_list))

def get_dataset_dict_by_prefix(schema):
    schema_keys_without_time = [key for key in schema.keys() if key!='time']
    schema_prefix_list = reduce(get_prefix, [key for key in schema_keys_without_time], [])
    muster_dict = {prefix: [schema[key] 
                            for key in schema.keys() 
                            if key.find(prefix)==0] 
                   for prefix in schema_prefix_list}
    return muster_dict

def get_dataset_dict_by_prefix_list(ds_list):
    names = [ds.name for ds in ds_list]
    get_ds_by_name = lambda name: [ds for ds in ds_list if ds.name==name][0]
    schema_keys_without_time = [key for key in names if key!='time']
    schema_prefix_list = reduce(get_prefix, [key for key in schema_keys_without_time], [])
    muster_dict = {prefix: [get_ds_by_name(key) 
                            for key in names
                            if key.find(prefix)==0] 
                   for prefix in schema_prefix_list}
    return muster_dict

def get_first_muster_dict(dataset_dict_by_prefix):
    return {key: dataset_dict_by_prefix[key+'1'] 
            for key in set([i[0:-1] for i in dataset_dict_by_prefix.keys()])}