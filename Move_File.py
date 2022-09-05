import os
from posixpath import splitext
import shutil

from_dir = "C:/Users/Harshal/Downloads"
to_dir = "D:/Harshal/WhiteHatJunior/C111 Project Importing"

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for file_name in list_of_files:
    name, extention = os.path.splitext(file_name)
    print(file_name)