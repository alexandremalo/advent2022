def get_one_tree_visibility(forest, current_line, current_column):
    current_tree_value = forest[current_line][current_column]
    visible_from_north = True
    visible_from_south = True
    visible_from_east = True
    visible_from_west = True

    for line in range(0, current_line):
        # print('north:' + str(forest[line][current_column]))
        if forest[line][current_column] >= current_tree_value:
            visible_from_north = False
    for line in range(current_line + 1, len(forest)):
        # print('south: '+str(forest[line][current_column]))
        if forest[line][current_column] >= current_tree_value:
            visible_from_south = False
    for column in range(current_column + 1, len(forest)):
        # print('east:' + str(forest[current_line][column]))
        if forest[current_line][column] >= current_tree_value:
            visible_from_east = False
    for column in range(0, current_column):
        # print('west:' + str(forest[current_line][column]))
        if forest[current_line][column] >= current_tree_value:
            visible_from_west = False

    return visible_from_north or visible_from_south or visible_from_east or visible_from_west


def get_visible_tree_count(forest):
    total_visible_tree = (len(forest) - 1) * 4
    for line in range(1, len(forest) - 1):
        for column in range(1, len(forest) - 1):
            if get_one_tree_visibility(forest, line, column):
                total_visible_tree += 1
    return total_visible_tree


def solve():
    with open('input/input1', 'r') as file:
        forest = []
        for line in file:
            column_index = 0
            forest_line = []
            for tree in line.strip():
                forest_line.append(int(tree))
                column_index += 1
            forest.append(forest_line)
        result = get_visible_tree_count(forest)
        print(forest)
        print("=== Result ===")
        print(result)
        print("==============")


if __name__ == '__main__':
    solve()
