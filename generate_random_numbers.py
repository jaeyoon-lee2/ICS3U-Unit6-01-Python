#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Nov 2019
# This program displays 10 ramdom number with the array

import random


def main():
    # this function displays 10 ramdom number with the array

    my_numbers = []

    # input
    for loop_counter in range(0, 10):
        a_number = random.randint(1, 100)
        my_numbers.append(a_number)

    print("The random numbers:")

    for loop_counter in range(0, 10):
        print("{0} ".format(my_numbers[loop_counter]), end="")
    average = (my_numbers[0] + my_numbers[1] + my_numbers[2] + my_numbers[3]
               + my_numbers[4] + my_numbers[5] + my_numbers[6] + my_numbers[7]
               + my_numbers[8] + my_numbers[9]) / 10
    print("")
    print("The average of those numbers is {0}".format(average))


if __name__ == "__main__":
    main()
