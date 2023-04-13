# Generated with the help of ChatGPT
# Date: 2023-04-13

import os
import argparse

parser = argparse.ArgumentParser(description='Rename files in a folder.')
parser.add_argument('folder', type=str, help='name of folder containing files')
parser.add_argument('increment', type=int, help='number to increment index by')
parser.add_argument('--rename', action='store_true', help='rename files (default: dry run)')
args = parser.parse_args()

folder_name = args.folder
increment = args.increment
do_rename = args.rename

dry_run_results = []

# loop over files in folder
for file_name in os.listdir(folder_name):
    # check if file starts with CXXXX where XXXX is a four-digit number
    if len(file_name) >= 5 and file_name[0] == "C" and file_name[1:5].isdigit():
        # get index of file
        index = int(file_name[1:5])
        # calculate new index
        new_index = index + increment
        # generate new file name
        new_file_name = "C{:04d}{}".format(new_index, file_name[5:])
        if do_rename:
            # rename file
            os.rename(os.path.join(folder_name, file_name), os.path.join(folder_name, new_file_name))
            print("Renamed {} to {}".format(file_name, new_file_name))
        else:
            dry_run_results.append((file_name, new_file_name))

if not do_rename:
    # sort dry run results by original file name
    dry_run_results.sort(key=lambda x: x[0])
    # print dry run results
    for original, new in dry_run_results:
        print("Dry run: {} will be renamed to {}".format(original, new))
