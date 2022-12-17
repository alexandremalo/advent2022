def update_result(result, register_x_value, current_cycle):
    if abs(current_cycle % 40 - register_x_value) <= 1:
        row_index_to_update = current_cycle // 40
        col_index_to_update = current_cycle % 40
        #print(row_index_to_update, col_index_to_update)
        result[row_index_to_update][col_index_to_update] = '#'
    return result


def process_cpu_instruction(current_cycle, register_x_value, result, line):
    line_split = line.split()
    #print(line_split)
    current_cycle += 1
    result = update_result(result, register_x_value, current_cycle)
    if line.strip() != "noop":
        current_cycle += 1
        result = update_result(result, register_x_value, current_cycle)
        register_x_value += int(line_split[1])
    return current_cycle, register_x_value, result

def solve():
    with open('input/input1', 'r') as file:
        register_x_value = 1
        current_cycle = -1
        result = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                   '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',  '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                   '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                   '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                   '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                   '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                   '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                  ]
        print(len(result[0]))
        for line in file:
            current_cycle, register_x_value, result = process_cpu_instruction(current_cycle, register_x_value, result, line)
        for screen_row in result:
            print(''.join(screen_row))
        print(len(result[0]))
        print("=== Result ===")
        print(result)
        print("==============")


if __name__ == '__main__':
    solve()
