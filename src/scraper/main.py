from crud import CRUD
from misc import *

if __name__ == "__main__":
    data = load_data_from_file('/app/assets/data.json')
    data_dict = convert_json_to_data_dict(data)
    db = CRUD()
    db.create('test', data_dict)
