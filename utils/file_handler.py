import os
import json


def read_directory(folder_path, file_type):
    files = []
    for item in os.listdir(folder_path):
        if item.endswith(f".{file_type}"):
            files.append(item)
    return files


def read_file(folder_path, files):
    data = []
    for item in files:
        with open(f"{folder_path}/{item}", "r", encoding="utf-8") as f_obj:
            data.append(f_obj.read())
    return data


def write_single_book_file(book_stat, file_name, folder):
    with open(f"{folder}/txt_{file_name}.json", "w", encoding="utf-8") as f_obj:
        json.dump(book_stat, f_obj, ensure_ascii=False, indent=4)


def convert_json_to_dict(json_files):
    data = []
    for idx in range(len(json_files)):
        data.append(json.loads(json_files[idx]))
    return data


def write_single_stat_file(folder, minmax_stat, old_book_stat, long_title_stat, five_char_stat):
    statistics = {
        "longest_shortest_book": minmax_stat,
        "oldest_book": old_book_stat,
        "longest_title": long_title_stat,
        "legtobb_5_karakteres_szo": five_char_stat
    }

    with open(f"{folder}/statistics.json", "w", encoding="utf-8") as f_obj:
        json.dump(statistics, f_obj, ensure_ascii=False, indent=4)
