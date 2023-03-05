def book_statistic():
    """
    legenerálja a fájlonkénti statisztikát (1. statisztika)
    """
    from file_handler import read_directory
    from file_handler import read_file
    from file_handler import write_single_book_file

    from params import stats_folder_path
    from params import book_folder_path

    import math
    import re

    regTitle = r"Title: .*"
    regRelease = r"Release Date: .*"
    files = read_directory(book_folder_path, "txt")
    books = read_file(book_folder_path, files)
    for idx in range(len(books)):
        releaseDate = re.findall(regRelease, books[idx])
        releaseDate = releaseDate[0][14:] if len(releaseDate) > 0 else ""
        title = re.findall(regTitle, books[idx])
        title = title[0][7:]
        stat_dict = {
            "releaseDate": releaseDate,
            "title": title,
            "pages": math.ceil(len(books[idx]) / 3000)
        }
        write_single_book_file(stat_dict, title, stats_folder_path)


def min_max_page(result_stats):
    """
    megkeresi az min max oldalszámot és visszaadja
    """
    all_pages = []
    page_statistics = []

    for item in result_stats:
        all_pages.append(item["pages"])
    max_page = max(all_pages)
    min_page = min(all_pages)

    for item in result_stats:
        if item["pages"] == max_page:
            longest_book = {
                "longest_book": {
                    "page_size": max_page,
                    "title": item["title"]
                }
            }
            page_statistics.append(longest_book)
        if item["pages"] == min_page:
            shortest_book = {
                "shortest_book": {
                    "page_size": min_page,
                    "title": item["title"]
                }
            }
            page_statistics.append(shortest_book)

    return page_statistics


def oldest_book(result_stats):
    """
    megkeresi a kiadás dátumát és visszaadja
    """
    import re

    rel_date_full = []
    reg_date = r"[0-9]{4}"
    for item in result_stats:
        rel_date_full.append(re.findall(reg_date, item["releaseDate"]))

    rel_date_min = []
    for dates in rel_date_full:
        if len(dates) > 0:
            rel_date_min.append(int(dates[0]))
    rel_date_min = min(rel_date_min)

    books = {}
    for items in result_stats:
        if len(re.findall(reg_date, items["releaseDate"])) > 0:
            if re.findall(reg_date, items["releaseDate"])[0] == str(rel_date_min):
                books.update({
                    f'oldest_book_{items["title"]}': {
                        "release_date": re.findall(reg_date, items["releaseDate"])[0],
                        "title": items["title"]
                    }
                })
    return books


def longest_title(result_stats):
    """
    megkeresi a leghosszabb könyv címet
    """
    title = []
    longest_title = []
    for item in result_stats:
        title.append(len(item["title"]))

    title_long = max(title)

    for item in result_stats:
        if len(item["title"]) == title_long:
            longest = {
                "title": item["title"],
                "length": title_long,
            }
            longest_title.append(longest)
    return longest_title


def more_than_five_character():
    """
    megkeresi, hogy melyik könyvben van a legtöbb 5 karakter vagy 
    annál hosszabb szavak
    """
    from file_handler import read_directory
    from file_handler import read_file

    from params import book_folder_path

    import re

    regTitle = r"Title: .*"
    book = read_directory(book_folder_path, "txt")
    books_result = read_file(book_folder_path, book)

    temp = []
    max_char_num = []
    book_title = []
    for idx in range(len(books_result)):
        for item in books_result[idx].split('\n'):
            temp.extend(item.split(' '))
        temp = [item.replace(",", "") for item in temp if len(item) >= 5]
        max_char_num.append(len(temp))
        book_title.append(re.findall(regTitle, books_result[idx])[0][7:])

    max_five_char_word = {}
    for idx, item in enumerate(max_char_num):
        if item == max(max_char_num):
            max_five_char_word = {
                "words_num":  max(max_char_num),
                "title": book_title[idx]
            }
    return max_five_char_word


def all_book_statistic():
    """
    összegyűjti a statisztikai adatokat és 
    kiíratja json fájlba
    """
    from params import stats_folder_path
    from params import sing_stat_folder_path

    from file_handler import read_directory
    from file_handler import read_file
    from file_handler import convert_json_to_dict
    from file_handler import write_single_stat_file

    files = read_directory(stats_folder_path, "json")
    stats = read_file(stats_folder_path, files)
    result_stats = convert_json_to_dict(stats)

    min_max_result = min_max_page(result_stats)
    old_book = oldest_book(result_stats)
    longest_title_result = longest_title(result_stats)
    more_than_five_char = more_than_five_character()
    write_single_stat_file(sing_stat_folder_path, min_max_result, old_book,
                           longest_title_result, more_than_five_char)


if __name__ == '__main__':
    book_statistic()
    all_book_statistic()
