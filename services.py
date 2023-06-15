import csv
import json


def csv_to_json(csv_file_path, json_file_path):
    json_array = []

    # read csv file
    with open(csv_file_path, encoding='utf-8-sig') as csv_file:
        # load csv file data using csv library's dictionary reader
        csv_reader = csv.DictReader(csv_file)

        # convert each csv row into python dict
        for row in csv_reader:
            # add this python dict to json array
            json_array.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        json_string = json.dumps(json_array, ensure_ascii=False, indent=4)
        jsonf.write(json_string)


csv_file_path = '/Users/morinch/PycharmProjects/skypro/skypro_hw_28/datasets/location.csv'
json_file_path = '/Users/morinch/PycharmProjects/skypro/skypro_hw_28/datasets/location.json'

csv_to_json(csv_file_path=csv_file_path, json_file_path=json_file_path)
