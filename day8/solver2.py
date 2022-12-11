def get_one_tree_scenic_score(forest, current_line, current_column):
    current_tree_value = forest[current_line][current_column]
    # print(current_tree_value)
    scenic_score_north = 0
    scenic_score_south = 0
    scenic_score_east = 0
    scenic_score_west = 0

    for line in range(0, current_line):
        # print('north:' + str(forest[current_line - (line + 1)][current_column]))
        scenic_score_north += 1
        if forest[current_line - (line + 1)][current_column] >= current_tree_value:
            break
    for line in range(current_line + 1, len(forest)):
        # print('south: '+str(forest[line][current_column]))
        scenic_score_south += 1
        if forest[line][current_column] >= current_tree_value:
            break
    for column in range(current_column + 1, len(forest)):
        # print('east:' + str(forest[current_line][column]))
        scenic_score_east += 1
        if forest[current_line][column] >= current_tree_value:
            break
    for column in range(0, current_column):
        # print('west:' + str(forest[current_line][current_column - (column + 1)]))
        scenic_score_west += 1
        if forest[current_line][current_column - (column + 1)] >= current_tree_value:
            break
    return scenic_score_north * scenic_score_south * scenic_score_east * scenic_score_west


def get_best_scenic_score(forest):
    best_scenic_score = 0
    for line in range(1, len(forest) - 1):
        for column in range(1, len(forest) - 1):
            current_scenic_score = get_one_tree_scenic_score(forest, line, column)
            if current_scenic_score > best_scenic_score:
                best_scenic_score = current_scenic_score
    return best_scenic_score


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
        result = get_best_scenic_score(forest)
        print(forest)
        print("=== Result ===")
        print(result)
        print("==============")


if __name__ == '__main__':
    solve()
