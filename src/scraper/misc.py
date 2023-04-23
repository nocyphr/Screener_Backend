import json


def append_values(data_dict, element):
    for key, value in element.items():
        data_dict[key].append(value)

def convert_json_to_data_dict(list_of_dicts):
    data_dict = {key: [] for key in list_of_dicts[0].keys()}
    for element in list_of_dicts:
        append_values(data_dict, element)
    return data_dict

def load_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
