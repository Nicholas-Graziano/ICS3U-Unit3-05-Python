#!/usr/bin/env python3

# Created by: Nicholas Graziano
# Created on: November 2020
# This program checks if a number is negative or positive

def main():
    # this program checks if the number is a negative or positive

    # input
    number = int(input("enter a number from 1-12:"))

    # process
    if (number == 1):
        print("January")
    elif (number == 2):
        print("february")
    elif (number == 3):
        print("March")
    elif (number == 4):
        print("April")
    elif (number == 5):
        print("May")
    elif (number == 6):
        print("June")
    elif (number == 7):
        print("July")
    elif (number == 8):
        print("August")
    elif (number == 9):
        print("September")
    elif (number == 10):
        print("October")
    elif (number == 11):
        print("November")
    elif (number == 12):
        print("December")
    else:
        print("i have no idea")


if __name__ == "__main__":
    main()
