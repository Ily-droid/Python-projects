import math
# math rand
import random as r


# Function to compute y for given x, a, b


def compute_y(x, a, b):
    term1 = (2 ** x) * math.log10(a) * x
    term2 = (3 ** x) * math.log10(b) * x
    return term1 - term2


# Function to get input from the user
def get_input():
    x = float(input("Enter the value for x: "))
    a = float(input("Enter the value for a: "))
    b = float(input("Enter the value for b: "))
    return x, a, b


def task1_a():
    comm_string = input("Enter variables? y/n \n")
    if comm_string == 'y':
        num = 1
    else:
        num = 0

    while num == 1:
        # Get inputs from the user
        x, a, b = get_input()

        # Compute y
        y = compute_y(x, a, b)

        # Print the result
        print(f"The value of y is: {y}")
        print("\n")

    while num == 0:
        x = 5.4
        a = 2.3
        b = 0.5

        # Compute y
        y_answer = 2 ** x * math.log10(a) * x - 3 ** x * math.log10(b) * x

        print(f"The value of y is: {y_answer}")
        break


def answer_y(x, a, b):
    # Function to compute y for given x, a, b

    numerator = a * x + math.exp(-x) * math.cos(math.radians(b * x))
    denominator = b * x - math.exp(-x) * math.sin(math.radians(b * x)) + 1
    return numerator / denominator


def task1_b():
    comm_string = input("Enter variables? y/n \n")
    if comm_string == 'y':
        num = 1
    else:
        num = 0

    # Get inputs from the user
    while num == 1:
        x, a, b = get_input()

        # Compute y
        y = answer_y(x, a, b)

        # Print the result
        print(f"The value of y is: {y}")

    while num == 0:
        x_value = 1.9
        a_value = 0.3
        b_value = 1.9

        # Compute y
        y = answer_y(x_value, a_value, b_value)
        # Print the result
        print(f"The value of y is: {y}")
        break


def multiply_by_2(arr):
    barr = arr
    for i in range(arr.__len__()):
        barr[i] = arr[i] * 2
    print(f"2nd {arr.__len__()} symbols array *2 = {barr}")


def task2():
    # Створити список з 10 випадкових елементів (від -10 до 12). Збільшити
    # значення усіх елементів списку удвічі. Знайти суму, кількість та середнє
    # арифметичне окремо позитивних та негативних елементів та порівняти з
    # відповідними значеннями початкового списку

    a = [r.randint(-10, 12) for i in range(0, 10)]
    print(f"1st 10 symbols array = {a}")

    multiply_by_2(a)


def task3():
    """
    Створити список з числами типа float (не менш 12 елементів).
    Для цього списку знайти:
    - індекс максимального елемента списку;
    - різницю між найбільшим та найменшим елементами списку;
    - поміняти місцями найбільший та найменший елементи списку;
    - знайти найбільший парний елемент списку;
    - знайти найменший додатній елемент списку. """


# Main program
def main():
    while True:
        tasks = input("Enter the task number Or enter q to quit \n one.one\n one.two\n two\n ")
        if tasks == 'q':
            quit()
        if tasks == 'one.one':
            task1_a()
        if tasks == 'one.two':
            task1_b()
        if tasks == 'two':
            task2()
        else:
            print("Wrong number choose one or two, try again")


# Run the main program
if __name__ == "__main__":
    main()
