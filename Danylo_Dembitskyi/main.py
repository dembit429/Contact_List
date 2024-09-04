def read_nums(filename):
    numbers = []
    with open(filename, "r") as file:
        for i in file:
            numbers.append(int(i))
    return numbers


def read_steps(filename):
    with open(filename, "r") as file:
        return int(file.read())


def fibunachi(steps):
        num1 = numbers[-2]
        num2 = numbers[-1]
        next_number = num1 + num2
        numbers.append(next_number)
        if len(numbers) == steps:
            return
        fibunachi(steps)

numbers = read_nums("numbers.txt")
steps = read_steps("steps.txt")
fibunachi(steps)


print(numbers)