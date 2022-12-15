import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file_name) -> list[dict]:
    with open(file_name) as input_file:
        rows_list = input_file.read().splitlines()

    header = rows_list.pop(0)
    keys_list = header.split(',')

    json_data = list()
    for row in rows_list:
        row_list = row.split(',')
        obj = dict()
        for i in range(len(keys_list)):
            obj[keys_list[i]] = row_list[i]
        json_data.append(obj)

    return json_data


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))