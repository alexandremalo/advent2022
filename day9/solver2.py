def process_tail_step(current_head_position, current_tail_position):
    if current_tail_position[0] >= current_head_position[0] + 2:
        current_tail_position[1] = current_head_position[1]
        current_tail_position[0] = current_head_position[0] + 1
    elif current_tail_position[0] <= current_head_position[0] - 2:
        current_tail_position[1] = current_head_position[1]
        current_tail_position[0] = current_head_position[0] - 1
    if current_tail_position[1] >= current_head_position[1] + 2:
        current_tail_position[0] = current_head_position[0]
        current_tail_position[1] = current_head_position[1] + 1
    elif current_tail_position[1] <= current_head_position[1] - 2:
        current_tail_position[0] = current_head_position[0]
        current_tail_position[1] = current_head_position[1] - 1
    # print("TAIL: ", current_tail_position)
    return current_tail_position


def process_head_move(visited_positions, current_head_position, current_tail_position, line):
    line_split = line.split()
    # print(line_split)
    for step in range(0, int(line_split[1])):
        if line_split[0] == 'R':
            current_head_position[1] += 1
        elif line_split[0] == 'L':
            current_head_position[1] -= 1
        elif line_split[0] == 'U':
            current_head_position[0] -= 1
        elif line_split[0] == 'D':
            current_head_position[0] += 1
        # print("HEAD: ", current_head_position)
        current_tail_position[0] = process_tail_step(current_head_position, current_tail_position[0])
        for tail_id in range(1, len(current_tail_position)):
            current_tail_position[tail_id] = process_tail_step(current_tail_position[tail_id - 1],
                                                               current_tail_position[tail_id])
            print(current_tail_position)
        position_id = str(current_tail_position[8][0]) + "/" + str(current_tail_position[8][1])
        # print(position_id)
        if position_id not in visited_positions:
            visited_positions.add(position_id)
    return visited_positions, current_head_position, current_tail_position


def solve():
    with open('input/input1', 'r') as file:
        visited_positions = {"0/0"}
        current_head_position = [0, 0]
        current_tail_position = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        for line in file:
            visited_positions, current_head_position, current_tail_position = process_head_move(visited_positions,
                                                                                                current_head_position,
                                                                                                current_tail_position,
                                                                                                line)
        result = len(visited_positions)
        print("=== Result ===")
        print(result)
        print("==============")


if __name__ == '__main__':
    solve()
