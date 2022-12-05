def value_of_top_column(boat, jobs_to_do):
    for job in jobs_to_do:
        moving_values = []
        for x in range(job[0]):
            moving_values.append(boat[job[1]-1].pop())
        for value in reversed(moving_values):
            boat[job[2] - 1].append(value)
    to_return = []
    for column in boat:
        to_return.append(column[len(column)-1])
    return to_return





def solve():
    with open('input/input1', 'r') as file:
        # INPUT
        is_boat_input_line = True
        boat_input = []
        procedure_input = []
        horizontal_lines = []
        for line in file:
            if line == "\n":
                is_boat_input_line = False
            elif is_boat_input_line:
                char_index = 0
                column_index = 0
                horizontal_lines_values = [].copy()
                while char_index <= len(line) - 1:
                    if line[char_index+1] == ' ':
                        horizontal_lines_values.append(' ')
                    else:
                        horizontal_lines_values.append(line[char_index+1])
                    char_index += 4
                    column_index += 1
                boat_input.append(line)
                horizontal_lines.append(horizontal_lines_values)
            else:
                procedure_input.append(line.strip())

        # BOAT INPUT MAPPING
        line_index = len(horizontal_lines) - 1
        boat_columns = []
        for item in horizontal_lines[line_index]:
            boat_columns.append([])
        number_of_column = len(boat_columns)
        line_index -= 1
        while line_index >= 0:
            for x in range(number_of_column):
                if x < len(horizontal_lines[line_index]) and horizontal_lines[line_index][x] != ' ':
                    boat_columns[x].append(horizontal_lines[line_index][x])
            line_index -= 1

        # PROCEDURE INPUT MAPPING
        jobs_to_do = []
        for line in procedure_input:
            l = line.strip("move")
            nb_of_move = int(l.split(" from ")[0])
            second_half = l.split(" from ")[1].split(" to ")
            source = int(second_half[0])
            dest = int(second_half[1])
            jobs_to_do.append([nb_of_move, source, dest])

        #Solve
        response = value_of_top_column(boat_columns, jobs_to_do)
        print("=== Result ===")
        #print(boat_columns)
        #print(jobs_to_do)
        print(response)
        print("==============")

if __name__ == '__main__':
    solve()
