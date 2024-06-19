import os
import glob

def count_lines_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return sum(1 for line in file)

def count_lines_in_folder(folder_path, file_extension):
    file_pattern = os.path.join(folder_path, f'*.{file_extension}')
    files = glob.glob(file_pattern)
    line_counts = {}
    
    for file in files:
        line_counts[file] = count_lines_in_file(file)
    
    return line_counts

folder_path = 'C:\\Users\\cleme\\OneDrive\\Desktop\\MedLinkx'
file_extension = 'html'  # Change this to the desired file extension
line_counts = count_lines_in_folder(folder_path, file_extension)

for file, line_count in line_counts.items():
    print(f'{file}: {line_count} lines')
