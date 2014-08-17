#!/usr/bin/python
# -*- coding: utf-8 -*-
class Validater(object):    
    
    def __init__(self):
        self.__list = []
    
    def add(self, name, error_type, message):
        self.__list.append((name, error_type, message))
        
    def __str__(self):
        string = ''
        for item in self.__list:
            string += item[0] + item[1] + item[2] + '\n'
        return string
        
    
    @staticmethod
    def validate_syntax(sdf_ext):
        validater = Validater()
        # There must be a sheet or table named 'time'
        if sdf_ext['time'] is None:
            validater.add('time', 
                          ' scale missing ', 
                          'Time scale is not found')
        
        keys_without_time = [key for key in sdf_ext.keys() if key!='time']
            
        prefix_list = reduce(Validater.__get_prefix, [key for key in keys_without_time], [])
        # There must be an underscore symbol between the component name (prefix) and the variable name
        for key in keys_without_time:
            if key.find('_') < 0:
                validater.add(key, 
                              ' naming error ', 
                              'must be an underscore symbol between the component name (prefix) and the variable name')
            else:
                if key[: key.find('_')] not in prefix_list:
                    validater.add(key, 
                                  ' naming error ', 
                                  'underscore symbol in error position')
        # Component names must be ended with a number and the number should start from 1
        prefix_without_number = []
        print prefix_list
        for prefix in prefix_list:
            lastchar = prefix[-1]
            try: 
                lastchar = int(lastchar)
                for pwon in prefix_without_number:
                    if pwon[0] == prefix[0:-1]:
                        pwon[1].append(lastchar)
                        break
                else:
                    prefix_without_number.append((prefix[0:-1], [lastchar]))
            except:
                prefix_without_number.append((prefix, []))
                validater.add(prefix, 
                              ' number missing ', 
                              'number not found in component name')
                
        # The number of the component should be from 1 to n, and there should be no empty values
        for (prefix, char_list) in prefix_without_number:
            char_list = sorted(char_list)
            if char_list != range(1, len(char_list)+1):
                validater.add(prefix + str([i for i in range(1, len(char_list)+1) if i not in char_list]), 
                              ' number missing ', 
                              'number not correct in component name')
                
        # The number of values of each variable must be equal to  the number of values of ‘time‘ variable
        time_length = len(sdf_ext['time'].data)
        for key in keys_without_time:
            if len(sdf_ext[key].data) != time_length:
                validater.add(key, 
                              ' data length error ', 
                              'data length not equals to time, time length = %d, data length = %d' 
                              %(time_length, len(sdf_ext[key].data)) )
        return validater
        
        
    @staticmethod
    def validate_semantic(sdf_ext):   
        validater = Validater()
        schema = sdf_ext.get_schema()
        schema_keys_without_time = [key for key in schema.keys() if key!='time']
        schema_prefix_list = reduce(Validater.__get_prefix, [key for key in schema_keys_without_time], [])
        muster_dict = {prefix: [schema[key] 
                                for key in schema.keys() 
                                if key.find(prefix)==0] 
                       for prefix in schema_prefix_list}
        first_muster_dict = {key: muster_dict[key+'1'] for key in set([i[0:-1] for i in muster_dict.keys()])}

        data_keys_without_time = [key for key in sdf_ext.keys() if key!='time']
        data_prefix_list = reduce(Validater.__get_prefix, [key for key in data_keys_without_time], [])
        data_dict_by_prefix = {prefix: [sdf_ext[key] 
                                for key in sdf_ext.keys() 
                                if key.find(prefix)==0] 
                               for prefix in data_prefix_list}

        # The component with the identical name must have identical structure of variables.
        for key in data_dict_by_prefix.keys():
            data_names_by_prefix = [ds.name for ds in data_dict_by_prefix[key]]
            if key in muster_dict.keys():
                muster_names_by_prefix = [ds.name for ds in muster_dict[key]]
                if data_names_by_prefix != muster_names_by_prefix:
                    validater.add(key, 
                                  ' component structure error ', 
                                  'component structure not equals to schema: %s, schema %s' 
                                    %(str(data_names_by_prefix), str(muster_names_by_prefix)))
            else:
                if key[0:-1] in first_muster_dict.keys():
                    validater.add(key, 
                                  ' component name not found ', 
                                  'component name not found, but a similar component to validate')
                    muster_names_by_prefix = [key+ds.name[len(key):] for ds in first_muster_dict[key[0:-1]]]
                    if data_names_by_prefix != muster_names_by_prefix:
                        validater.add(key, 
                                      ' component structure error ', 
                                      'component structure not equals to schema: %s, schema %s' 
                                      %(str(data_names_by_prefix), str(muster_names_by_prefix)))
                        
        # The validation routine should compare the  Comments, Quantity, Unit, DisplayUnit of the variable
        for key in sdf_ext.keys():
            if key in schema.keys():

                if sdf_ext[key].comment != schema[key].comment:
                    validater.add(key, ' comment not validated ', 
                                  sdf_ext[key].comment + ', schema:' + schema[key].comment)
                if sdf_ext[key].unit != schema[key].unit:
                    validater.add(key, ' unit not validated ', 
                                  sdf_ext[key].comment + ', schema:' + schema[key].unit)
                if sdf_ext[key].quantity != schema[key].quantity:
                    validater.add(key, ' quantity not validated ', 
                                  sdf_ext[key].comment + ', schema:' + schema[key].quantity)
            else:
                prefix = [p for p in data_prefix_list if key.find(p)==0][0]
                replace_key = prefix[0:-1]
                if replace_key in first_muster_dict.keys():
                    muster_ds = [ds 
                                 for ds in first_muster_dict[replace_key] 
                                 if ds.name==replace_key+'1'+key.replace(prefix, '')]
                    if len(muster_ds) > 0: 
                        if sdf_ext[key].comment != muster_ds[0].comment:
                            validater.add(key, ' comment not validated ', 
                                          sdf_ext[key].comment + ', schema:' + muster_ds[0].comment)
                        if sdf_ext[key].unit != muster_ds[0].unit:
                            validater.add(key, ' unit not validated ', 
                                          sdf_ext[key].unit + ', schema:' + muster_ds[0].unit)
                        if sdf_ext[key].quantity != muster_ds[0].quantity:
                            validater.add(key, ' quantity not validated ', 
                                          sdf_ext[key].quantity + ', schema:' + muster_ds[0].quantity)
                    else:
                        validater.add(key, ' schema not found ', '')
                else:
                    validater.add(key, ' schema not found ', '')
        
        return validater
            
                
    
    @staticmethod
    def __get_prefix(prefix_list, name):
        return_list = []
        find = False
        for prefix in prefix_list:
            for i in range(len(prefix)):
                if prefix[i] != name[i]:
                    prefix_fix = prefix[:i]
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
        return return_list 