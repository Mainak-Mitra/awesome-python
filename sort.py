#!/usr/bin/env python
# coding: utf-8

"""
    The approach taken is explained below. I decided to do it simply.
    Initially I was considering parsing the data into some sort of
    structure and then generating an appropriate README. I am still
    considering doing it - but for now this should work. The only issue
    I see is that it only sorts the entries at the lowest level, and that
    the order of the top-level contents do not match the order of the actual
    entries.

    This could be extended by having nested blocks, sorting them recursively
    and flattening the end structure into a list of lines. Revision 2 maybe ^.^.
"""

import os

def read_file(file_path):
    """Reads the contents of a file and returns it."""
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return None
    with open(file_path, 'r') as file:
        return file.readlines()

def write_file(file_path, content):
    """Writes the given content to a file."""
    with open(file_path, 'w') as file:
        file.writelines(content)

def sort_blocks(read_me_lines):
    """Sorts the blocks of content in the README file."""
    blocks = []
    temp_block = []

    for line in read_me_lines:
        if line.startswith('# '):
            if temp_block:
                blocks.append(''.join(sorted(temp_block, key=str.lower)))
                temp_block = []
        temp_block.append(line)
    if temp_block:
        blocks.append(''.join(sorted(temp_block, key=str.lower)))

    return blocks

def main():
    """Main function to execute the sorting of README blocks."""
    readme_path = 'README.md'
    read_me_lines = read_file(readme_path)
    if read_me_lines is None:
        return
    sorted_blocks = sort_blocks(read_me_lines)
    write_file(readme_path, sorted_blocks)

if __name__ == "__main__":
    main()

