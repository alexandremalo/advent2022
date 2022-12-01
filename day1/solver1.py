class Lunch:
    def __init__(self):
        self.calories = 0

    def add_calories(self, calories):
        self.calories += calories


def get_new_bigger_lunch_found(record, lunch):
    to_return = record
    if lunch.calories > record:
        to_return = lunch.calories
    return to_return


def solve():
    with open('input/input1', 'r') as file:
        biggest_lunch_found = 0
        current_lunch = Lunch()
        for line in file:
            print(line)
            if line == "\n":
                biggest_lunch_found = get_new_bigger_lunch_found(biggest_lunch_found, current_lunch)
                current_lunch = Lunch()
            else:
                current_lunch.add_calories(int(line))
        biggest_lunch_found = get_new_bigger_lunch_found(biggest_lunch_found, current_lunch)
        print("=== Result ===")
        print(biggest_lunch_found)
        print("==============")

if __name__ == '__main__':
    solve()
