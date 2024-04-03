
import treevizer
from treevizer import recursion_viz, to_png
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENERATED_DATA_DIR = os.path.join(BASE_DIR, "app/generated_data/")
dot_data_dir = os.path.join(GENERATED_DATA_DIR, "dot_files")
png_data_dir = os.path.join(GENERATED_DATA_DIR, "png_files")


def get_next_file_name(directory, base_name, extension):
    counter = 1
    while True:
        filename = os.path.join(directory, "{}{}.{}".format(base_name, counter, extension))
        if not os.path.exists(filename):
            return filename
        counter += 1

"{}".format(user_code)
        