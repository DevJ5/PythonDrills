#!/usr/bin/python3
import os
import re

files_list = os.listdir(os.getcwd() + "/modifieds")
sorted_files_list = sorted(files_list, reverse=True)
print("Sorted files: " + str(sorted_files_list))

for filename in sorted_files_list:
    matchObj = re.match(r"\w*(\d)\w*", filename)
    print(f"Match Object: {matchObj.group(1)}")
    new_number = str(int(matchObj.group(1)) + 1)
    findallList = re.findall(r"\d", filename)
    print(f"Find all: {findallList}")
    new_name = re.sub(r"(\d)", new_number, filename)

    print(os.path.join("modifieds", filename))
    print(os.path.join("modifieds", new_name))
    os.rename(os.path.join("modifieds", filename), os.path.join("modifieds", new_name))
