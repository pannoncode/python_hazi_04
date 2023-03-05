import os

book_folder_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "books")


stats_folder_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "stat_files")

sing_stat_folder_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "sing_stat_file")

# print(os.path.exists(book_folder_path))
# print(os.path.exists(stats_folder_path))
# print(os.path.exists(sing_stat_folder_path))
