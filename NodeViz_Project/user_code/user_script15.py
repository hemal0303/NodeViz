
import treevizer
from treevizer import recursion_viz, to_png
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENERATED_DATA_DIR = os.path.join(BASE_DIR, "generated_data/")
dot_data_dir = os.path.join(GENERATED_DATA_DIR, "dot_files")
png_data_dir = os.path.join(GENERATED_DATA_DIR, "png_files")


def get_next_file_location(directory, base_name, type):
    counter = 1
    while True:
        concated = base_name + str(counter) + type
        filename = os.path.join(directory, concated)
        if not os.path.exists(filename):
            return filename
        counter += 1

def get_next_file_name(directory, base_name, type):
    counter = 1
    while True:
        concated = base_name + str(counter) + type
        filename = os.path.join(directory, concated)
        if not os.path.exists(filename):
            return concated  # Return only the filename, not the full path
        counter += 1        

dot_path = get_next_file_location(dot_data_dir, "dot_file", '.dot')
png_path = get_next_file_location(png_data_dir, "png_file", '.png')

import treevizer
from treevizer import recursion_viz, to_png
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENERATED_DATA_DIR = os.path.join(BASE_DIR, "generated_data/")
dot_data_dir = os.path.join(GENERATED_DATA_DIR, "dot_files")
png_data_dir = os.path.join(GENERATED_DATA_DIR, "png_files")


def get_next_file_location(directory, base_name, type):
    counter = 1
    while True:
        concated = base_name + str(counter) + type
        filename = os.path.join(directory, concated)
        if not os.path.exists(filename):
            return filename
        counter += 1

def get_next_file_name(directory, base_name, type):
    counter = 1
    while True:
        concated = base_name + str(counter) + type
        filename = os.path.join(directory, concated)
        if not os.path.exists(filename):
            return concated  # Return only the filename, not the full path
        counter += 1        

dot_path = get_next_file_location(dot_data_dir, "dot_file", '.dot')
png_path = get_next_file_location(png_data_dir, "png_file", '.png')

@recursion_viz
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  

fibonacci(6)
  
treevizer.recursion_to_png("fibonacci", dot_path=dot_path, png_path=png_path)
file_name = get_next_file_name(png_data_dir, "png_file", '.png')
print(file_name)
file_name = get_next_file_name(png_data_dir, "png_file", '.png')
print(file_name)

