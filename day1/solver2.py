class Lunch:
    def __init__(self):
        self.calories = 0

    def add_calories(self, calories):
        self.calories += calories


def get_new_bigger_lunch_found(record_first, record_second, record_third, lunch):
    if lunch.calories < record_third:
        return record_first, record_second, record_third
    else:
        array = [record_first, record_second, record_third, lunch.calories]
        array.sort(reverse=True)
        return array[:-1]


def solve():
    with open('input/input1', 'r') as file:
        first_biggest_lunch_found, second_biggest_lunch_found, third_biggest_lunch_found = 0, 0, 0
        current_lunch = Lunch()
        for line in file:
            print(line)
            if line == "\n":
                first_biggest_lunch_found, second_biggest_lunch_found, third_biggest_lunch_found = get_new_bigger_lunch_found(
                    first_biggest_lunch_found, second_biggest_lunch_found, third_biggest_lunch_found, current_lunch)
                current_lunch = Lunch()
            else:
                current_lunch.add_calories(int(line))
        first_biggest_lunch_found, second_biggest_lunch_found, third_biggest_lunch_found = get_new_bigger_lunch_found(
            first_biggest_lunch_found, second_biggest_lunch_found, third_biggest_lunch_found, current_lunch)
        print("=== Result ===")
        print(first_biggest_lunch_found + second_biggest_lunch_found + third_biggest_lunch_found)
        print("==============")

if __name__ == '__main__':
    solve()
