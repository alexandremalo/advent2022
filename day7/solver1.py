def populate_tree_with_line(current_location, directory_tree, line):
    # print(line)
    line_array = line.split()
    if line[0] == '$' and line_array[1] == "cd" and line_array[2] != '/':
        if line_array[2] != "..":
            folder_to_insert = {'folders': {}, 'local_size': 0, 'total_size': 0}
            current_folder = directory_tree
            for folder in current_location.split('/'):
                current_folder = current_folder[folder]['folders']
            # print(current_folder)
            if current_folder.get(line_array[2], 0) == 0:
                current_folder[line_array[2]] = folder_to_insert
            current_location += "/" + line_array[2]
            # print("current_location after DOWN: "+current_location)
        else:
            new_current_location = current_location.split('/')[:-1]
            current_location = '/'.join(str(x) for x in new_current_location)
            # print("current_location after UP: " + current_location)
    elif line[0] != '$' and line_array[0] != "dir":
        current_location_folders = current_location.split('/')
        current_folder = directory_tree
        for folder in current_location_folders[:-1]:
            current_folder = current_folder[folder]['folders']
        current_folder = current_folder[current_location_folders[len(current_location_folders) - 1]]
        current_folder['local_size'] = current_folder['local_size'] + int(line_array[0])
        # print(current_folder)
    return current_location, directory_tree


def find_total_size_of_directory(directory):
    total_size = directory['local_size']
    for key in directory['folders']:
        total_size += find_total_size_of_directory(directory['folders'][key])
    directory['total_size'] = total_size
    return total_size


def find_small_folders(directory, small_folders_values):
    for key in directory['folders']:
        find_small_folders(directory['folders'][key], small_folders_values)
    if directory['total_size'] < 100_000:
        small_folders_values.append(directory['total_size'])
    return small_folders_values


def total_value_from_array(values):
    total = 0
    for value in values:
        total += value
    return total

def solve():
    with open('input/input1', 'r') as file:
        directory_tree = {'root': {'folders': {}, 'local_size': 0, 'total_size': 0}}
        current_location = "root"
        for line in file:
            current_location, directory_tree = populate_tree_with_line(current_location, directory_tree, line)
        complete_tree = find_total_size_of_directory(directory_tree['root'])
        result = total_value_from_array(find_small_folders(directory_tree['root'], []))
        print(directory_tree)
        print("=== Result ===")
        print(result)
        print("==============")


if __name__ == '__main__':
    solve()
