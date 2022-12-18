def debug_view(grid, ongoing_path, already_visited_position, start_position, end_position):
    row_index = 0
    for row in grid:
        col_to_print = []
        col_index = 0
        for col in row:
            char = '0'
            found_current_position = False
            current_pointer = str(row_index) + '/' + str(col_index)
            for path in ongoing_path:
                if path['position'] == current_pointer:
                    found_current_position = True
            if start_position == current_pointer:
                char = 'S'
            elif end_position == current_pointer:
                char = 'E'
            elif found_current_position:
                char = '@'
            elif current_pointer in already_visited_position:
                char = '#'
            col_to_print.append(char)
            col_index +=1
        row_index += 1
        print(''.join(col_to_print))
    print("==========================")



def evaluate_next_steps_and_fork_path(grid, ongoing_paths, already_visited_position, start_position, end_position):
    arrived_at_destination = False
    shortest_path = 0
    ongoing_paths_new = []
    path_index = 0
    for current_path in ongoing_paths:
        new_visited_position = []
        current_path_row_index = int(current_path['position'].split('/')[0])
        current_path_col_index = int(current_path['position'].split('/')[1])
        step_new = current_path['step'] + 1
        # North check
        if current_path_row_index - 1 >= 0:
            if abs(grid[current_path_row_index][current_path_col_index] - grid[current_path_row_index - 1][current_path_col_index]) <= 1:
                new_position_name = str(current_path_row_index - 1) + '/' + str(current_path_col_index)
                new_trace = current_path['trace'] + ' -> ' + new_position_name
                if new_position_name not in already_visited_position:
                    new_visited_position.append(new_position_name)
                    ongoing_paths_new.append({'step': step_new, 'position': new_position_name, 'trace': new_trace})
                    if new_position_name == end_position:
                        arrived_at_destination = True
                        print("arrived_at_destination")
                        shortest_path = step_new
                        break
        # South Check
        if current_path_row_index + 1 < len(grid):
            if abs(grid[current_path_row_index][current_path_col_index] - grid[current_path_row_index + 1][current_path_col_index]) <= 1:
                new_position_name = str(current_path_row_index + 1) + '/' + str(current_path_col_index)
                new_trace = current_path['trace'] + ' -> ' + new_position_name
                if new_position_name not in already_visited_position:
                    new_visited_position.append(new_position_name)
                    ongoing_paths_new.append({'step': step_new, 'position': new_position_name, 'trace': new_trace})
                    if new_position_name == end_position:
                        arrived_at_destination = True
                        print("arrived_at_destination")
                        shortest_path = step_new
                        break
        # East Check
        if current_path_col_index + 1 < len(grid[0]):
            if abs(grid[current_path_row_index][current_path_col_index] - grid[current_path_row_index][current_path_col_index + 1]) <= 1:
                new_position_name = str(current_path_row_index) + '/' + str(current_path_col_index + 1)
                new_trace = current_path['trace'] + ' -> ' + new_position_name
                if new_position_name not in already_visited_position:
                    new_visited_position.append(new_position_name)
                    ongoing_paths_new.append({'step': step_new, 'position': new_position_name, 'trace': new_trace})
                    if new_position_name == end_position:
                        arrived_at_destination = True
                        print(arrived_at_destination)
                        print("arrived_at_destination")
                        shortest_path = step_new
                        break
        # West Check
        if current_path_col_index - 1 >= 0:
            if abs(grid[current_path_row_index][current_path_col_index] - grid[current_path_row_index][current_path_col_index - 1]) <= 1:
                new_position_name = str(current_path_row_index) + '/' + str(current_path_col_index - 1)
                new_trace = current_path['trace'] + ' -> ' + new_position_name
                if new_position_name not in already_visited_position:
                    new_visited_position.append(new_position_name)
                    ongoing_paths_new.append({'step': step_new, 'position': new_position_name, 'trace': new_trace})
                    if new_position_name == end_position:
                        arrived_at_destination = True
                        print("arrived_at_destination")
                        shortest_path = step_new
                        break
        for item in new_visited_position:
            already_visited_position.append(item)
        path_index += 1
    print(len(ongoing_paths_new))
    print(step_new)
    #print(already_visited_position)
    #print(ongoing_paths_new)
    debug_view(grid, ongoing_paths_new, already_visited_position, start_position, end_position)
    return ongoing_paths_new, arrived_at_destination, shortest_path


def get_fast_route_to_ending(grid, start_position, end_position):
    already_visited_position = [start_position]
    ongoing_paths = []
    initial_path = {'step': 0, 'position': start_position, 'trace': start_position}
    ongoing_paths.append(initial_path)
    arrived_at_destination = False
    shortest_path = 0
    while not arrived_at_destination and len(ongoing_paths) != 0:
        ongoing_paths, arrived_at_destination, shortest_path = evaluate_next_steps_and_fork_path(grid, ongoing_paths,
                                                                                                 already_visited_position,
                                                                                                 start_position,
                                                                                                 end_position)
    return shortest_path


def generate_grid_from_input(file):
    grid = []
    start_position = "0/0"
    end_position = "0/0"
    row_index = 0
    for line in file:
        grid_line = []
        col_index = 0
        for char in line.strip():
            if char == 'E':
                end_position = str(row_index) + '/' + str(col_index)
                grid_line.append(27)
            elif char == 'S':
                start_position = str(row_index) + '/' + str(col_index)
                grid_line.append(0)
            else:
                grid_line.append(ord(char)-96)
            col_index += 1
        grid.append(grid_line)
        row_index += 1
    return grid, start_position, end_position

def solve():
    with open('input/input1', 'r') as file:
        grid, start_position, end_position = generate_grid_from_input(file)
        print('Grid: ', grid)
        print('Start: ', start_position)
        print('End: ', end_position)
        result = get_fast_route_to_ending(grid, start_position, end_position)
        print("=== Result ===")
        print(result)
        print("==============")


if __name__ == '__main__':
    solve()
