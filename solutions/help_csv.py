#CSV Module import
import csv

# OS Module imports
from os import makedirs     # allows us to create a dir
from os.path import dirname # gets parent folder in a path
from os.path import join    # concatenate paths
from os.path import exists  # check if a path exists

def split_csv(csv_path, table_names):
    paths = [] # collect output file paths
    tables_infos = detect_tables_from_csv(csv_path, table_names)
    for table_info in tables_infos:
        output_path = split_csv_by_indexes(csv_path, table_info)
        paths.append(output_path)

    print "\nFiles written:"
    for p in paths:
        print p
    print
    return paths

def split_csv_by_indexes(csv_path, table_info):
    title, start_index, end_index = table_info
    dir_ = dirname(dirname(csv_path))
    dir_ = join(dir_, "temp")
    if not exists(dir_):
        makedirs(dir_)
    output_path = join(dir_, title) + ".csv"
    output_path = output_path.replace(" ", "_")
    with open(output_path, 'w') as output_file, open(csv_path, 'rb') as input_file:
        writer = csv.writer(output_file)
        reader = csv.reader(input_file)
        for i, line in enumerate(reader):
            if i < start_index:
                continue
            if i > end_index:
                break
            writer.writerow(line)
    return output_path

def detect_tables_from_csv(csv_path, table_names):
    output = []
    with open(csv_path, 'rb') as csv_file:
        reader = csv.reader(csv_file)
        for idx, row in enumerate(reader):
            for col in row:
                match = [title for title in table_names if title in col]
                if match:
                    match = match[0] # get the first matching element
                    try:
                        end_index = idx - 1
                        start_index
                    except NameError:
                        start_index = 0
                    else:
                        output.append((previous_match, start_index, end_index))
                    print "Found new table", col
                    start_index = idx
                    previous_match = match
                    match = False

        end_index = idx  # last 'end_index' set to EOF
        output.append((previous_match, start_index, end_index))
        return output