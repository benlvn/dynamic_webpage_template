import os
import shutil

print("Webpage name: ", end='')
pagename = input()
# TODO: Error check for nonalphanum or nonspaces

# ASSUME: webpage is valid folder name
# TODO: make spaces underscores
# TODO: lowercase
# TODO: check for folder already exists
os.mkdir(pagename)
dir_path = os.path.dirname(os.path.realpath(__file__))
template_folder = os.path.join(dir_path, "template_files")
src_files = os.listdir(template_folder)
for file_name in src_files:
    full_file_name = os.path.join(template_folder  , file_name)
    if (os.path.isfile(full_file_name)):
        shutil.copy(full_file_name, pagename)
