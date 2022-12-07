def first_four_diff_char_position(radio_signal):
    char_index = 3
    found_four_diff = False
    while found_four_diff == False or char_index <= len(radio_signal) - 1:
        found_duplicated = False
        char_set = {}
        for x in range(4):
            if char_set.get(radio_signal[char_index - x], 0) != 0:
                found_duplicated = True
            char_set[radio_signal[char_index - x]] = 1
        char_index += 1
        if found_duplicated == False:
            print(char_index)
            break
    return char_index


def solve():
    with open('input/input1', 'r') as file:
        for line in file:
            radio_signal_position = first_four_diff_char_position(line)
        print("=== Result ===")
        print(len(line))
        print(radio_signal_position)
        print("==============")


if __name__ == '__main__':
    solve()
